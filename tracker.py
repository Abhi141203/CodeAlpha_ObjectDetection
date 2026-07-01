import cv2
from ultralytics import YOLO

# 1. Load the pre-trained YOLO model (it will download automatically the first time)
model = YOLO('yolov8n.pt') 

# 2. Open the webcam (0 is usually the default laptop camera)
cap = cv2.VideoCapture(0)

print("Press 'q' to quit the video stream.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 3. Run YOLO inference on the frame
    # The 'track=True' argument enables built-in object tracking
    results = model.track(frame, persist=True)

    # 4. Draw the bounding boxes and IDs on the frame
    annotated_frame = results[0].plot()

    # 5. Display the output
    cv2.imshow("YOLOv8 Real-Time Tracking", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()