from deep_sort_realtime.deepsort_tracker import DeepSort
tracker = DeepSort(max_age=30)
def track_people(detections, frame):
    ds_detections = []
    for det in detections:
        x, y, w, h = det
        conf = 0.9
        ds_detections.append([
            [x, y, w, h],
            conf,
            "person"
        ])
    tracks = tracker.update_tracks(ds_detections, frame=frame)
    output = []
    for track in tracks:
        if track.is_confirmed() and track.track_id is not None:
            x1, y1, x2, y2 = track.to_tlbr()
            output.append([track.track_id, (int(x1), int(y1), int(x2), int(y2))])
    return output