import cv2
import numpy as np

def change_hair_color(image_path, new_color):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of colors for hair
    lower_hair_color = np.array([0, 20, 20])
    upper_hair_color = np.array([20, 255, 255])

    # Mask the hair color
    hair_mask = cv2.inRange(hsv_image, lower_hair_color, upper_hair_color)

    # Generate a binary mask for hair
    hair_mask = cv2.merge([hair_mask, hair_mask, hair_mask])

    # Replace the hair color with the new color
    new_hair_color = np.array(new_color, dtype=np.uint8)
    new_hair = cv2.bitwise_and(hair_mask, new_hair_color)

    # Replace the original hair with the new hair color
    output = cv2.addWeighted(image, 1.0, new_hair, 1.0, 0.0)

    # Display the output image
    cv2.imshow('Hair Color Change', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the image file path and the new hair color (B, G, R)
image_path = '/Users/andygu/Desktop/preply_umair/HairColorChange-main/files/1.jpg'
new_color = [0, 0, 0]  # Green color

change_hair_color(image_path, new_color)
