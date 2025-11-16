🚨 Prohibited Area Intrusion Detection System
YOLOv8 + DeepSORT + OpenCV

This project is a Python-based system for detecting human intrusion into a restricted (prohibited) zone using YOLOv8, DeepSORT, and OpenCV.
Users can manually mark restricted areas directly on a video frame; the system saves those coordinates and uses them to detect when a tracked person enters the prohibited zone.

📌 Features
✔️ Human Detection

Uses YOLOv8n (Ultralytics) to detect people in each video frame.

✔️ Person Tracking

Uses DeepSORT for stable, continuous person ID tracking.

Reduces false positives and improves tracking reliability.

✔️ Manual Restricted Zone Marking

User clicks points on the first frame to draw a polygon.

Zone coordinates are stored in restricted_zones.json.

✔️ Intrusion Detection

System checks whether any tracked person enters the polygonal restricted zone.

When a person enters → Red ALARM! appears on screen.

When person leaves the zone → alarm stops after 3 seconds.

✔️ Clean Architecture

The project is separated into:

detection.py — YOLO detection

tracker.py — DeepSORT tracking

zone.py — zone checker

main.py — video processing and intrusion detection loop
