import tensorflow as tf
import tensorflow_hub as hub
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import cv2
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the pre-trained object detection model from TensorFlow Hub
# Replace with the desired EfficientDet-Lite version (e.g., efficientdet_lite0, efficientdet_lite2)
efficientdet_lite_model = "https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1" # Example: EfficientDet-Lite2
detector = hub.load(efficientdet_lite_model)

# Example usage within feature_extraction.py (or in your main script)
image_path = "C:\Users\nidgkuma\Downloads\video asset app\data\frames1\frame_0007.jpg"
detections = detect_objects(image_path)

if detections:
    print(f"Detected objects: {detections}")


# ... (rest of the code)

def detect_objects(image_path):
    """Detects objects in an image using the loaded detector."""
    try:
        img = cv2.imread(image_path)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
        input_tensor = tf.convert_to_tensor(rgb_img, dtype=tf.uint8)
        input_tensor = input_tensor[tf.newaxis, ...]

        # Run inference
        results = detector(input_tensor)

        # Process the results (results are tensors)
        # Example: Access bounding boxes and class labels
        bounding_boxes = results['detection_boxes'][0].numpy()
        class_labels = results['detection_classes'][0].numpy().astype(int)
        scores = results['detection_scores'][0].numpy()

        # Filter detections based on a score threshold (e.g., 0.3)
        filtered_boxes = bounding_boxes[scores > 0.3]
        filtered_labels = class_labels[scores > 0.3]
        filtered_scores = scores[scores > 0.3]

        return {
            "boxes": filtered_boxes,
            "labels": filtered_labels,
            "scores": filtered_scores
        }

    except Exception as e:
        logging.error(f"Error detecting objects in {image_path}: {e}")
        return None
    

def analyze_sentiment(text):
    """Analyzes sentiment of a given text using VADER."""
    try:
        nltk.download('vader_lexicon')
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        return scores
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        return None


def extract_features(frames_folder, transcript):
    """Extracts features from video frames and transcript."""
    all_detections = []
    for filename in os.listdir(frames_folder):
        if filename.endswith((".jpg", ".png")): # Check image extensions
            frame_path = os.path.join(frames_folder, filename)
            detections = detect_objects(frame_path)
            if detections:
                all_detections.append(detections)


    features = {
        "objects": all_detections, # Store all detections
        "sentiment": analyze_sentiment(transcript) if transcript else None,
    }
    return features
