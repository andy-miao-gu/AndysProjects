
import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe solutions for face detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Load bunny ears image with alpha channel (transparency)
bunny_ears = cv2.imread('DALL_E_2023-12-11_14.59.59_-_A_pair_of_cartoon-style_bunny_ears_with_a_transparent_background._The_bunny_ears_should_be_tall__fluffy__and_white__suitable_for_overlaying_on_a_perso.png', -1)  # Replace with the path to your bunny ears image

# Open the default camera
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the color space from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        results = face_detection.process(frame_rgb)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                # Resize bunny ears to match the width of the face
                ears_width = w
                ears_height = int(ears_width * bunny_ears.shape[0] / bunny_ears.shape[1])
                resized_ears = cv2.resize(bunny_ears, (ears_width, ears_height))

                # Calculate position for bunny ears (above the head)
                ears_x1 = x
                ears_x2 = ears_x1 + ears_width
                ears_y1 = max(y - ears_height, 0)
                ears_y2 = ears_y1 + ears_height

                # Extract the region of interest (ROI) from the frame
                roi = frame[ears_y1:ears_y2, ears_x1:ears_x2]

                # Extract alpha channel from bunny ears image
                mask = resized_ears[:, :, 3]
                mask_inv = cv2.bitwise_not(mask)
                bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
                fg = cv2.bitwise_and(resized_ears, resized_ears, mask=mask)

                # Combine the background and foreground (bunny ears)
                combined = cv2.add(bg, fg[:, :, 0:3])

                # Place the bunny ears on the frame
                frame[ears_y1:ears_y2, ears_x1:ears_x2] = combined

        # Display the frame
        cv2.imshow('Bunny Face', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
