import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

FRAME_WIDTH = int(cap.get(3))
FRAME_HEIGHT = int(cap.get(4))
CENTER_X = FRAME_WIDTH // 2
CENTER_ZONE = FRAME_WIDTH // 4 
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    action = "MOVE FORWARD"

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            width = x2 - x1
            height = y2 - y1
            area = width * height

            obj_center_x = (x1 + x2) // 2
            obj_center_y = (y1 + y2) // 2

            if area > 5000 and abs(obj_center_x - CENTER_X) < CENTER_ZONE:
                if obj_center_x < CENTER_X:
                    action = "TURN RIGHT"
                else:
                    action = "TURN LEFT"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
            cv2.circle(frame, (obj_center_x, obj_center_y), 5, (0,0,255), -1)

    cv2.putText(frame, f"Action: {action}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

    cv2.imshow("Rover Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
