
- Dataset link -> https://universe.roboflow.com/patricks-workspace-zye5m/safety-helmet-detection-mqtqd/dataset/2

# helmet-detection-yolov8
# Real-Time Helmet Detection with YOLOv8
<p align="center">
  <img src="https://github.com/user-attachments/assets/2be9dc41-7be9-46a8-bad8-3a808a98724f" alt="Model Inference Test Result" width="800">
  <br>
  <em><p align="center"><b>Model Test Sonucu:</b> Model, yakın mesafede hem çıplak kafayı (head) hem de baretli insanı yüksek güven oranıyla başarıyla ayrıştırıyor.</p></em>
</p>

Bu proje, iş sağlığı ve güvenliği (İSG) standartlarına uygun olarak şantiye ve fabrika ortamlarında **baret kullanımını canlı kamera (real-time) üzerinden tespit etmek** amacıyla geliştirilmiştir. Proje, InnoVentures Tech bünyesindeki yaz stajım sürecinde geliştirilmiş ve optimize edilmiştir.

## Öne Çıkan Özellikler & Çözülen Problemler (Troubleshooting)

Projenin ilk aşamalarında modelin uzak mesafeden iyi çalışmasına rağmen, yakın mesafede çıplak insan kafasını baret ile karıştırması (**Scale & Dataset Bias**) problemiyle karşılaşılmıştır. Bu sorunu kökten çözmek için şu optimizasyonlar uygulanmıştır:

* **Veri Seti Birleştirme (Dataset Merging):** Uzak çekim fotoğraflardan oluşan ana veri seti, internetten ve Roboflow Universe üzerinden toplanan yakın çekim (close-up) `head` ve `head with helmet` görselleriyle birleştirilerek hibrit bir veri havuzu oluşturulmuştur.
* **Negatif Örnekleme (Negative Sampling):** Modelin çıplak kafayı baret sanmasını engellemek amacıyla, etiketlenmemiş yakın çekim kafa fotoğrafları sisteme beslenerek sahte pozitif (False Positive) oranları düşürülmüştür.
* **Hiperparametre Ayarları:** Canlı yayındaki anlık yanılmaları engellemek için `conf=0.60` güven eşiği eklenmiş; kutuların ekranda titremesini ve üst üste binmesini engellemek için de `iou=0.45` filtresi (Non-Maximum Suppression) aktif edilmiştir.

---

## Proje Yapısı
```mermaid
flowchart TD
    subgraph Data_Prep ["1. Veri Hazırlığı & Ön İşleme"]
        A[Roboflow / Ham Veri Seti] --> B[Faster R-CNN Dataset<br/>Train / Valid / Test]
        A --> C[YOLO / RT-DETR Dataset<br/>Train / Valid / Test]
    end

    subgraph Modeling ["2. Model Eğitimi & Çıkarım"]
        B --> D[Faster R-CNN Eğitimi<br/>helmet_detection_fasterrcnn.ipynb]
        C --> E[YOLO Modelleri Eğitimi<br/>train_baret.py / YOLOv8, YOLO11, YOLO26]
        C --> F[RT-DETR Mimarisi<br/>helmet_detection_rtdetr.ipynb]
    end

    subgraph Explainable_AI ["3. Model Açıklanabilirliği (XAI)"]
        D --> G[EigenCAM Görselleştirme<br/>fasterrcnn_eigercam.ipynb]
        E --> H[Grad-CAM / EigenCAM Analizi<br/>YOLO_v8_EigenCAM.ipynb / yolo_cam]
        G & H --> I[XAI_Output & Metrik Grafikleri<br/>faster_rcnn_loss.png]
    end

    subgraph Deployment ["4. Çıkarım & Canlı Takip (Inference)"]
        E & F --> J[Model Ağırlıkları<br/>best.pt / rtdetr-l.pt]
        J --> K[Görsel / Video Tahminleri<br/>predict.py]
        J --> L[Gerçek Zamanlı Kamera Akışı<br/>realtime_baret.py]
        L --> M{Baret / Kask Tespiti}
        M -->|Tespit Edildi| N[Güvenli Alan Analizi & Kayıt]
        M -->|Tespit Edilemedi| O[Uyarı / Takip Çıktısı]
    end
