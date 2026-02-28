from ultralytics import YOLO

class PlantDetector:
    def __init__(self, model_path="best.pt"):
        self.model = YOLO(model_path)

    def detect(self, source_path):
        results = self.model(source_path)

        detections = []

        for r in results:
            for box in r.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = self.model.names[class_id]

                detections.append({
                    "class": class_name,
                    "confidence": round(confidence, 3)
                })

        if len(detections) == 0:
            return {"status": "No plant detected"}

        return {"detections": detections}