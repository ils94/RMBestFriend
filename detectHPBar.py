import os
import cv2
import numpy as np
import pyautogui
import globalVariables


def is_hp_low():
    create_images_directory()

    image_files = []

    # Specify the external directory path
    external_directory = globalVariables.image_detection_path

    # Iterate over files in the external directory
    for filename in os.listdir(external_directory):
        # Check if the file has a common image file extension (e.g., jpg, png, jpeg)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # If it's an image file, add it to the list
            image_files.append(os.path.join(external_directory, filename))

    for image_path in image_files:
        image_to_detect = cv2.imread(image_path)

        screenshot = pyautogui.screenshot()

        screenshot_np = np.array(screenshot)
        screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Define your x, y coordinates for the top-left and bottom-right corners of the ROI
        x1, y1 = globalVariables.start_x, globalVariables.start_y  # Top-left corner
        x2, y2 = globalVariables.end_x, globalVariables.end_y  # Bottom-right corner

        # Ensure that the coordinates are integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Crop the screenshot to the specified ROI using your x, y coordinates
        screenshot_cv_roi = screenshot_cv[y1:y2, x1:x2]

        result = cv2.matchTemplate(screenshot_cv_roi, image_to_detect, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.7:
            return True


def create_images_directory():
    if not os.path.exists(globalVariables.image_detection_path):
        os.makedirs(globalVariables.image_detection_path)
