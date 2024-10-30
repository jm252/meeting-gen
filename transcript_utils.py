import re
from skimage.metrics import structural_similarity as ssim
import cv2

def is_junk_text(text):
    """
    Determines if the given text is considered junk.

    Args:
        text (str): The text to be checked.

    Returns:
        bool: True if the text is considered junk, False otherwise.
    """
    # Check for empty string
    print("Text")
    print(text)
    if text == '':
        return True

    # Check if the text contains too many special characters
    if len(re.findall(r'[^A-Za-z0-9\s]', text)) > len(re.findall(r'[A-Za-z0-9]', text)):
        return True

    return False


def is_similar(new_image, image_list, threshold=0.9):
    """
    Check if the new image is sufficiently similar to any image in the list.

    Args:
        new_image (ndarray): The new image to compare.
        image_list (list): A list of images previously appended.
        threshold (float): Similarity threshold for SSIM (default is 0.9).

    Returns:
        bool: True if the new image is sufficiently similar to any image in the list, False otherwise.
    """
    resized_new = cv2.resize(new_image, (300, 300))
    for existing_image in image_list:
        # Resize both images to a fixed size for consistent comparison
        resized_existing = cv2.resize(existing_image, (300, 300))

        # Calculate SSIM between the new image and the existing image
        similarity_score, _ = ssim(
            resized_new,
            resized_existing,
            full=True,
            channel_axis=-1,  # Indicate that the last dimension is the color channel
            win_size=5        # Set a smaller window size for compatibility with image size
        )

        # If the similarity is above the threshold, we consider them similar
        print("SIMILARITY")
        print(similarity_score)
        if similarity_score >= threshold:
            return True

    # If no sufficiently similar image is found, return False
    return False
