from idlelib.debugger_r import frametable

import cv2
import json

video = cv2.VideoCapture("../files/test.mp4")
ret, frame = video.read()
video.release()

points = []
def click_event(event, x, y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        cv2.circle(frame, (x,y), 5,(0,255,0),-1)
        cv2.imshow("Frame",frame)
cv2.putText(frame,"Click to draw prohibited zone.Press any key to stop",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
cv2.imshow("Frame",frame)
cv2.setMouseCallback("Frame",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

zone = {"points":points}
with open("../files/restricted_zones.json", "w") as f:
    json.dump(zone,f)
print("Zone written to restricted_zones.json")

