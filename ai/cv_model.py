import cv2
import numpy as np

def classify_waste(image_path):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        return 'Unknown'

    # Simple rule-based classification (demo)
    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Calculate average hue
    avg_hue = np.mean(hsv[:, :, 0])

    # Rough classification based on color
    if avg_hue < 30:  # Reddish - perhaps hazardous
        waste_type = 'Hazardous'
    elif avg_hue < 90:  # Yellow/green - organic
        waste_type = 'Organic'
    else:  # Blue/purple - recyclable
        waste_type = 'Recyclable'

    return waste_type