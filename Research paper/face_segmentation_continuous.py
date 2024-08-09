
import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe solutions for face detection and selfie segmentation
mp_face_detection = mp.solutions.face_detection
mp_selfie_segmentation = mp.solutions.selfie_segmentation

# Open the default camera
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection, \
     mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the color space from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_results = face_detection.process(frame_rgb)
        segmentation_results = selfie_segmentation.process(frame_rgb)

        # Draw face bounding boxes
        if face_results.detections:
            for detection in face_results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Apply segmentation mask
        if segmentation_results.segmentation_mask is not None:
            condition = np.stack((segmentation_results.segmentation_mask,) * 3, axis=-1) > 0.5
            frame = np.where(condition, frame, np.zeros_like(frame))

        # Display the frame
        cv2.imshow('Face Segmentation', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
