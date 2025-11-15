import cv2,json,time
import numpy as np
from src.detection import detect_people
from tracker import track_people

with open("../files/restricted_zones.json") as f:
    zone_data = json.load(f)["points"]
zone_poly = np.array(zone_data,np.int32)

cap = cv2.VideoCapture("../files/test.mp4")
alarm_end_time = 0

while True:
    ret,frame = cap.read()
    if not ret:
        break

    detections = detect_people(frame)
    tracks = track_people(detections,frame)

    for track_id, (x1, y1, x2, y2) in tracks:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, str(track_id), (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        inside = cv2.pointPolygonTest(zone_poly, (cx, cy), False) >= 0
        if inside:
            alarm_end_time = time.time() + 3
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    if time.time() < alarm_end_time:
        cv2.putText(frame, "ALARM!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

    cv2.polylines(frame, [zone_poly], isClosed=True, color=(0, 0, 255), thickness=2)

    cv2.imshow("Intrusion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

