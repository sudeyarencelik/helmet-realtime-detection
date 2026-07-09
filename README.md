# helmet-detection-yolov8
# 🦺 Real-Time Helmet Detection with YOLOv8
<p align="center">
  <img src="image_816de3.jpg" alt="Model Inference Test Result" width="800">
  <br>
  <em><p align="center"><b>Model Test Sonucu:</b> Model, yakın mesafede hem çıplak kafayı (head) hem de baretli insanı yüksek güven oranıyla başarıyla ayrıştırıyor.</p></em>
</p>
Bu proje, iş sağlığı ve güvenliği (İSG) standartlarına uygun olarak şantiye ve fabrika ortamlarında **baret kullanımını canlı kamera (real-time) üzerinden tespit etmek** amacıyla geliştirilmiştir. Proje, InnoVentures Tech bünyesindeki yaz stajım sürecinde geliştirilmiş ve optimize edilmiştir.

## 🚀 Öne Çıkan Özellikler & Çözülen Problemler (Troubleshooting)

Projenin ilk aşamalarında modelin uzak mesafeden iyi çalışmasına rağmen, yakın mesafede çıplak insan kafasını baret ile karıştırması (**Scale & Dataset Bias**) problemiyle karşılaşılmıştır. Bu sorunu kökten çözmek için şu optimizasyonlar uygulanmıştır:

* **Veri Seti Birleştirme (Dataset Merging):** Uzak çekim fotoğraflardan oluşan ana veri seti, internetten ve Roboflow Universe üzerinden toplanan yakın çekim (close-up) `head` ve `head with helmet` görselleriyle birleştirilerek hibrit bir veri havuzu oluşturulmuştur.
* **Negatif Örnekleme (Negative Sampling):** Modelin çıplak kafayı baret sanmasını engellemek amacıyla, etiketlenmemiş yakın çekim kafa fotoğrafları sisteme beslenerek sahte pozitif (False Positive) oranları düşürülmüştür.
* **Hiperparametre Ayarları:** Canlı yayındaki anlık yanılmaları engellemek için `conf=0.60` güven eşiği eklenmiş; kutuların ekranda titremesini ve üst üste binmesini engellemek için de `iou=0.45` filtresi (Non-Maximum Suppression) aktif edilmiştir.

---

## 📂 Proje Yapısı

```text
helmet_AI/
│
├── halmet_dataset/      # Birleştirilmiş uzak ve yakın çekim hibrit veri seti
│   ├── train/           # Eğitim görselleri ve etiketleri (.txt)
│   ├── valid/           # Doğrulama görselleri ve etiketleri
│   └── data.yaml        # Sınıf bilgileri ve klasör yolları
│
├── realtime_baret.py    # Canlı kamera (Webcam) tahmin kodu
├── train_baret.py       # Model eğitim scripti
└── predict.py           # Tekli görsel test kodu
