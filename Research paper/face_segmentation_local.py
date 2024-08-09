
import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe solutions for face detection and selfie segmentation
mp_face_detection = mp.solutions.face_detection
mp_selfie_segmentation = mp.solutions.selfie_segmentation

# Read the image
image_path = 'IMG-20230516-WA0008.png' # Replace with the path to your image
image = cv2.imread(image_path)

# Detect faces
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    # Convert the color space from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)
    
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Segment the face
with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
    # Convert the color space from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = selfie_segmentation.process(image_rgb)
    
    # Generate a binary mask
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.5
    segmented_face = np.where(condition, image, np.zeros_like(image))

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Face', segmented_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
