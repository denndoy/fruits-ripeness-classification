"""
Utility functions untuk aplikasi real-time detection
"""

import cv2
import numpy as np
from pathlib import Path


def test_camera(camera_index=0):
    """
    Test apakah kamera berfungsi dengan baik
    
    Args:
        camera_index: Index kamera (0 untuk default webcam)
        
    Returns:
        bool: True jika kamera berfungsi, False jika tidak
    """
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        return False
    
    ret, frame = cap.read()
    cap.release()
    
    return ret and frame is not None


def list_available_cameras(max_test=5):
    """
    Cari semua kamera yang tersedia di sistem
    
    Args:
        max_test: Maximum jumlah index yang akan di-test
        
    Returns:
        list: List index kamera yang tersedia
    """
    available = []
    
    for i in range(max_test):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available.append(i)
            cap.release()
    
    return available


def create_confidence_bar(confidence, width=300, height=30, color=(0, 255, 0)):
    """
    Buat confidence bar sebagai image
    
    Args:
        confidence: Confidence score (0-100)
        width: Lebar bar
        height: Tinggi bar
        color: Warna bar (BGR)
        
    Returns:
        numpy array: Image confidence bar
    """
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    fill_width = int((confidence / 100) * width)
    cv2.rectangle(bar, (0, 0), (fill_width, height), color, -1)
    cv2.rectangle(bar, (0, 0), (width, height), (255, 255, 255), 2)
    
    return bar


def put_text_with_background(frame, text, position, font=cv2.FONT_HERSHEY_SIMPLEX,
                             font_scale=0.7, text_color=(255, 255, 255),
                             bg_color=(0, 0, 0), thickness=2, alpha=0.6):
    """
    Tulis text dengan background semi-transparan
    
    Args:
        frame: Frame untuk menulis text
        text: Text yang akan ditulis
        position: Posisi (x, y)
        font: Font OpenCV
        font_scale: Ukuran font
        text_color: Warna text (BGR)
        bg_color: Warna background (BGR)
        thickness: Ketebalan text
        alpha: Transparansi background (0-1)
        
    Returns:
        Frame dengan text
    """
    # Get text size
    (text_width, text_height), baseline = cv2.getTextSize(
        text, font, font_scale, thickness
    )
    
    x, y = position
    
    # Draw background rectangle
    overlay = frame.copy()
    cv2.rectangle(overlay, 
                 (x - 5, y - text_height - 5),
                 (x + text_width + 5, y + baseline + 5),
                 bg_color, -1)
    
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    
    # Draw text
    cv2.putText(frame, text, (x, y), font, font_scale, text_color, thickness)
    
    return frame


def draw_rounded_rectangle(image, top_left, bottom_right, color, thickness, radius):
    """
    Gambar rectangle dengan sudut melengkung
    
    Args:
        image: Image untuk digambar
        top_left: Koordinat kiri atas (x, y)
        bottom_right: Koordinat kanan bawah (x, y)
        color: Warna (BGR)
        thickness: Ketebalan garis (-1 untuk fill)
        radius: Radius sudut
        
    Returns:
        Image dengan rounded rectangle
    """
    x1, y1 = top_left
    x2, y2 = bottom_right
    
    # Draw main rectangles
    cv2.rectangle(image, (x1 + radius, y1), (x2 - radius, y2), color, thickness)
    cv2.rectangle(image, (x1, y1 + radius), (x2, y2 - radius), color, thickness)
    
    # Draw circles at corners
    cv2.circle(image, (x1 + radius, y1 + radius), radius, color, thickness)
    cv2.circle(image, (x2 - radius, y1 + radius), radius, color, thickness)
    cv2.circle(image, (x1 + radius, y2 - radius), radius, color, thickness)
    cv2.circle(image, (x2 - radius, y2 - radius), radius, color, thickness)
    
    return image


def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resize image dengan mempertahankan aspect ratio
    
    Args:
        image: Image yang akan di-resize
        width: Target width (None jika menggunakan height)
        height: Target height (None jika menggunakan width)
        inter: Interpolation method
        
    Returns:
        Resized image
    """
    dim = None
    h, w = image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    return cv2.resize(image, dim, interpolation=inter)


def add_watermark(frame, text="Fruit Ripeness Detection", position="bottom-right",
                 font_scale=0.5, color=(255, 255, 255), thickness=1):
    """
    Tambahkan watermark ke frame
    
    Args:
        frame: Frame untuk ditambahkan watermark
        text: Text watermark
        position: Posisi ("top-left", "top-right", "bottom-left", "bottom-right")
        font_scale: Ukuran font
        color: Warna text (BGR)
        thickness: Ketebalan text
        
    Returns:
        Frame dengan watermark
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
    
    h, w = frame.shape[:2]
    margin = 10
    
    # Tentukan posisi
    if position == "top-left":
        x, y = margin, text_height + margin
    elif position == "top-right":
        x, y = w - text_width - margin, text_height + margin
    elif position == "bottom-left":
        x, y = margin, h - margin
    else:  # bottom-right
        x, y = w - text_width - margin, h - margin
    
    # Add semi-transparent background
    overlay = frame.copy()
    cv2.rectangle(overlay, (x - 5, y - text_height - 5),
                 (x + text_width + 5, y + 5), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)
    
    # Add text
    cv2.putText(frame, text, (x, y), font, font_scale, color, thickness)
    
    return frame


def create_info_panel(width=400, height=600, title="Information"):
    """
    Buat panel informasi kosong
    
    Args:
        width: Lebar panel
        height: Tinggi panel
        title: Judul panel
        
    Returns:
        numpy array: Image panel
    """
    panel = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Draw header
    cv2.rectangle(panel, (0, 0), (width, 50), (50, 50, 50), -1)
    cv2.putText(panel, title, (10, 35), cv2.FONT_HERSHEY_SIMPLEX,
               1.0, (255, 255, 255), 2)
    
    return panel


def get_camera_info(camera_index=0):
    """
    Dapatkan informasi kamera
    
    Args:
        camera_index: Index kamera
        
    Returns:
        dict: Informasi kamera (width, height, fps, dll)
    """
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        return None
    
    info = {
        'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': cap.get(cv2.CAP_PROP_FPS),
        'backend': cap.getBackendName()
    }
    
    cap.release()
    
    return info


if __name__ == "__main__":
    # Test utilities
    print("🔍 Testing utilities...")
    
    # Test camera
    print("\n1. Testing camera...")
    if test_camera():
        print("   ✅ Camera OK")
    else:
        print("   ❌ Camera not available")
    
    # List cameras
    print("\n2. Available cameras:")
    cameras = list_available_cameras()
    if cameras:
        for cam in cameras:
            info = get_camera_info(cam)
            print(f"   Camera {cam}: {info['width']}x{info['height']} @ {info['fps']} FPS")
    else:
        print("   ❌ No cameras found")
    
    print("\n✅ Utilities test complete!")
