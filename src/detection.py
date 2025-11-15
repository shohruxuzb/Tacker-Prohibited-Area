from ultralytics import YOLO
model = YOLO("../yolov8n.pt")

def detect_people(frame):
    results = model(frame)[0]
    boxes = []
    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 0:
            x1, y1, x2, y2 = box.xyxy[0]
            boxes.append([
                int(x1),
                int(y1),
                int(x2 - x1),
                int(y2 - y1)
            ])
    return boxes
