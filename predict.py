from ultralytics import YOLO
import cv2

if __name__ == '__main__':

    print("BARET VE KAFA SAYICI SİSTEM BAŞLATILIYOR...")

    model = YOLO("runs/detect/train-3/weights/best.pt")

    results = model.predict(
        source="resim.jpeg",
        save=True,
        show=False,  
        imgsz=640,
        device=0
    )

    class_names = model.names

    head_count = 0
    helmet_count = 0


    for result in results:

        img = result.plot()
        print(f"Results: {result}")
        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cls_id = int(box.cls[0])
            name = class_names[cls_id]

            if name == "head":
                head_count += 1
            elif name == "head_with_helmet":
                helmet_count += 1

            text = f"({x1},{y1}) ({x2},{y2})"

            cv2.putText(
                img,
                text,
                (x1, y1 - 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                2
            )

        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Tahmin Sonucu", img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

    print("\n" + "=" * 40)
    print("ŞANTİYE GÜVENLİK RAPORU")
    print("=" * 40)
    print(f"Baretsiz Kafa Sayısı: {head_count}")
    print(f"Baretli Kafa Sayısı: {helmet_count}")
    print(f"Toplam İnsan Sayısı: {head_count + helmet_count}")
    print("=" * 40)
