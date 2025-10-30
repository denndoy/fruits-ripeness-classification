"""
Real-time Fruit Ripeness Detection using Webcam
Deteksi kematangan buah secara real-time menggunakan webcam dan model TensorFlow
"""

import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path
import time

# Konfigurasi
MODEL_PATH = Path("../models/model_checkpoints/mobilenetv2_best.keras")
IMG_SIZE = (224, 224)
CLASS_NAMES = [
    'overripe_apple',
    'overripe_banana', 
    'ripe_apple',
    'ripe_banana',
    'unripe_apple',
    'unripe_banana'
]

# Mapping ke label yang lebih user-friendly (Bahasa Indonesia)
CLASS_LABELS = {
    'overripe_apple': 'Apel Terlalu Matang',
    'overripe_banana': 'Pisang Terlalu Matang',
    'ripe_apple': 'Apel Matang',
    'ripe_banana': 'Pisang Matang',
    'unripe_apple': 'Apel Mentah',
    'unripe_banana': 'Pisang Mentah'
}

# Warna untuk setiap kategori kematangan (BGR format untuk OpenCV)
COLOR_MAP = {
    'overripe_apple': (0, 0, 255),      # Merah
    'overripe_banana': (0, 0, 255),     # Merah
    'ripe_apple': (0, 255, 0),          # Hijau
    'ripe_banana': (0, 255, 0),         # Hijau
    'unripe_apple': (255, 165, 0),      # Oranye
    'unripe_banana': (255, 165, 0)      # Oranye
}


class FruitRipenessDetector:
    """Class untuk deteksi kematangan buah secara real-time"""
    
    def __init__(self, model_path, img_size=(224, 224)):
        """
        Inisialisasi detector
        
        Args:
            model_path: Path ke model TensorFlow (.keras)
            img_size: Ukuran input gambar (width, height)
        """
        self.img_size = img_size
        self.model = None
        self.load_model(model_path)
        self.fps = 0
        self.frame_count = 0
        self.start_time = time.time()
        
    def load_model(self, model_path):
        """Load model TensorFlow"""
        try:
            print(f"📦 Loading model dari {model_path}...")
            self.model = tf.keras.models.load_model(model_path)
            print("✅ Model berhasil dimuat!")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def preprocess_frame(self, frame):
        """
        Preprocessing frame untuk prediksi
        
        Args:
            frame: Frame dari webcam (numpy array)
            
        Returns:
            Preprocessed frame siap untuk prediksi
        """
        # Resize ke ukuran yang dibutuhkan model
        resized = cv2.resize(frame, self.img_size)
        # Convert BGR (OpenCV) ke RGB (TensorFlow)
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        # Expand dimensions untuk batch
        input_tensor = np.expand_dims(rgb, axis=0)
        # Model sudah punya rescaling layer, jadi tidak perlu normalisasi manual
        return input_tensor
    
    def predict(self, frame):
        """
        Prediksi kematangan buah dari frame
        
        Args:
            frame: Frame dari webcam
            
        Returns:
            tuple: (predicted_class, confidence, probabilities)
        """
        # Preprocess
        input_tensor = self.preprocess_frame(frame)
        
        # Prediksi
        predictions = self.model.predict(input_tensor, verbose=0)
        
        # Get hasil
        pred_idx = np.argmax(predictions[0])
        confidence = predictions[0][pred_idx] * 100
        predicted_class = CLASS_NAMES[pred_idx]
        
        return predicted_class, confidence, predictions[0]
    
    def draw_prediction(self, frame, predicted_class, confidence):
        """
        Gambar hasil prediksi di frame
        
        Args:
            frame: Frame untuk digambar
            predicted_class: Kelas yang diprediksi
            confidence: Confidence score (%)
            
        Returns:
            Frame dengan overlay prediksi
        """
        height, width = frame.shape[:2]
        
        # Get label dan warna
        label = CLASS_LABELS.get(predicted_class, predicted_class)
        color = COLOR_MAP.get(predicted_class, (255, 255, 255))
        
        # Tentukan status berdasarkan kematangan
        if 'overripe' in predicted_class:
            status = "⚠️ TERLALU MATANG"
            status_color = (0, 0, 255)  # Merah
        elif 'ripe' in predicted_class:
            status = "✅ MATANG (SIAP KONSUMSI)"
            status_color = (0, 255, 0)  # Hijau
        else:  # unripe
            status = "⏳ MASIH MENTAH"
            status_color = (255, 165, 0)  # Oranye
        
        # Background untuk text
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (width, 120), (0, 0, 0), -1)
        frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)
        
        # Tulis prediksi
        cv2.putText(frame, label, (10, 35), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)
        cv2.putText(frame, f"Confidence: {confidence:.1f}%", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, status, (10, 105),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
        
        # Gambar confidence bar
        bar_width = int((confidence / 100) * (width - 20))
        cv2.rectangle(frame, (10, height - 30), (10 + bar_width, height - 10), color, -1)
        cv2.rectangle(frame, (10, height - 30), (width - 10, height - 10), (255, 255, 255), 2)
        
        return frame
    
    def draw_probabilities(self, frame, probabilities):
        """
        Gambar probabilitas semua kelas
        
        Args:
            frame: Frame untuk digambar
            probabilities: Array probabilitas untuk semua kelas
            
        Returns:
            Frame dengan probabilitas
        """
        height, width = frame.shape[:2]
        
        # Posisi untuk text
        y_offset = 140
        line_height = 30
        
        # Background
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 130), (width, 130 + len(CLASS_NAMES) * line_height + 10), 
                     (0, 0, 0), -1)
        frame = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)
        
        # Tulis semua probabilitas
        for i, (class_name, prob) in enumerate(zip(CLASS_NAMES, probabilities)):
            label = CLASS_LABELS.get(class_name, class_name)
            color = COLOR_MAP.get(class_name, (255, 255, 255))
            
            # Bar
            bar_length = int(prob * 300)
            y_pos = y_offset + i * line_height
            cv2.rectangle(frame, (10, y_pos), (10 + bar_length, y_pos + 20), color, -1)
            
            # Text
            text = f"{label}: {prob*100:.1f}%"
            cv2.putText(frame, text, (320, y_pos + 15), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame
    
    def update_fps(self):
        """Update FPS counter"""
        self.frame_count += 1
        elapsed = time.time() - self.start_time
        if elapsed > 1.0:
            self.fps = self.frame_count / elapsed
            self.frame_count = 0
            self.start_time = time.time()
    
    def draw_fps(self, frame):
        """Gambar FPS di frame"""
        cv2.putText(frame, f"FPS: {self.fps:.1f}", (frame.shape[1] - 120, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        return frame
    
    def run(self, camera_index=0, show_probabilities=True):
        """
        Jalankan detector dengan webcam
        
        Args:
            camera_index: Index kamera (0 untuk webcam default)
            show_probabilities: Tampilkan probabilitas semua kelas
        """
        print("🎥 Membuka webcam...")
        cap = cv2.VideoCapture(camera_index)
        
        if not cap.isOpened():
            print("❌ Error: Tidak dapat membuka webcam!")
            return
        
        # Set resolusi (opsional)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        print("✅ Webcam siap!")
        print("\n" + "="*60)
        print("🎯 PETUNJUK PENGGUNAAN:")
        print("="*60)
        print("  📹 Arahkan kamera ke buah (apel atau pisang)")
        print("  🔄 Tekan 'P' untuk toggle tampilan probabilitas")
        print("  📸 Tekan 'S' untuk screenshot")
        print("  ❌ Tekan 'Q' atau 'ESC' untuk keluar")
        print("="*60 + "\n")
        
        screenshot_count = 0
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("❌ Error: Tidak dapat membaca frame dari webcam!")
                break
            
            # Flip horizontal untuk efek mirror (lebih natural)
            frame = cv2.flip(frame, 1)
            
            # Prediksi
            predicted_class, confidence, probabilities = self.predict(frame)
            
            # Draw hasil
            frame = self.draw_prediction(frame, predicted_class, confidence)
            
            if show_probabilities:
                frame = self.draw_probabilities(frame, probabilities)
            
            # Update dan draw FPS
            self.update_fps()
            frame = self.draw_fps(frame)
            
            # Tampilkan frame
            cv2.imshow('🍎🍌 Fruit Ripeness Detection - Real-time', frame)
            
            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q') or key == 27:  # Q atau ESC
                print("\n👋 Menutup aplikasi...")
                break
            elif key == ord('p'):  # Toggle probabilities
                show_probabilities = not show_probabilities
                status = "ON" if show_probabilities else "OFF"
                print(f"📊 Tampilan probabilitas: {status}")
            elif key == ord('s'):  # Screenshot
                screenshot_count += 1
                filename = f"screenshot_{screenshot_count}.jpg"
                cv2.imwrite(filename, frame)
                print(f"📸 Screenshot disimpan: {filename}")
        
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        print("✅ Aplikasi ditutup dengan sukses!")


def main():
    """Main function"""
    try:
        # Cek apakah model ada
        if not MODEL_PATH.exists():
            print(f"❌ Error: Model tidak ditemukan di {MODEL_PATH}")
            print("💡 Pastikan Anda sudah melatih model dan file .keras ada di folder models/model_checkpoints/")
            return
        
        # Inisialisasi detector
        detector = FruitRipenessDetector(MODEL_PATH, IMG_SIZE)
        
        # Jalankan
        detector.run(camera_index=0, show_probabilities=True)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Program dihentikan oleh user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
