import re
import pytesseract
import cv2
import easyocr

reader = easyocr.Reader(['en'])


def get_screen_image(video_path, timestamp):
    """
    Capture a frame from the video at a specific timestamp.

    Args:
        video_path (str): Path to the video file.
        timestamp (float): Time in seconds to capture the frame.

    Returns:
        ndarray: Captured frame as an image, or None if unsuccessful.
    """
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)  # Set time in milliseconds

    success, frame = cap.read()
    cap.release()
    if success:
        return frame
    else:
        print(f"Failed to capture frame at {timestamp} seconds.")
        return None

def get_text_on_screen(frame_image):
    """
    Performs OCR to get text on the screen.

    Args:
        frame_image: The screen image

    Returns:
        str: The text extracted from the screen.
    """

    result = reader.readtext(frame_image)
    # Combine text from detected regions
    text = " ".join([item[1] for item in result])
    return text