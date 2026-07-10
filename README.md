# TO-DO List for work:
- Yolov11
- Yolov26
- Dataseti nereden aldigina dair link ekle buraya -> https://universe.roboflow.com/patricks-workspace-zye5m/safety-helmet-detection-mqtqd/dataset/2

# TO-DO List for publication:
- Faster R-CNN
- RT-DETR
- makale ve dergi taramasi: webofscience
- https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10677743
- ANACONDA-Navigator for Jupyter Notebook/Lab (confusion matrix, loss over EPOCH, accuracy over EPOCH figurleri ve tablolari)
- GPU icin ya kendi makinen, ya da Google Colab (daha hizli)


# helmet-detection-yolov8
# 🦺 Real-Time Helmet Detection with YOLOv8
<p align="center">
  <img src="https://github.com/user-attachments/assets/2be9dc41-7be9-46a8-bad8-3a808a98724f" alt="Model Inference Test Result" width="800">
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
