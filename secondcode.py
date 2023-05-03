import cv2
import numpy as np
 


def copy_move_detection(image, block_size=8, threshold=0.5):
    """
    Performs copy-move forgery detection on a given image using block matching.

    :param image: The input image (in BGR format).
    :param block_size: The size of the blocks to be compared.
    :param threshold: The threshold for detecting a forgery.
    :return: A copy of the input image with detected forgeries highlighted in red.
    """

    # Convert the input image to grayscale.
     
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the gradients in the x and y directions.
    grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)

    # Calculate the magnitude of the gradients.
    mag = np.sqrt(grad_x ** 2 + grad_y ** 2)

    # Normalize the magnitudes to [0, 1] range.
    mag /= mag.max()

    # Divide the image into blocks.
    blocks = []
    for i in range(0, mag.shape[0] - block_size, block_size):
        for j in range(0, mag.shape[1] - block_size, block_size):
            block = mag[i:i + block_size, j:j + block_size]
            blocks.append(block)

    # Calculate the mean of each block.
    means = [np.mean(block) for block in blocks]

    # Compare each block to all other blocks to detect copies.
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if abs(means[i] - means[j]) < threshold:
                # A copy has been found.
                x1 = (i % (mag.shape[1] // block_size)) * block_size
                y1 = (i // (mag.shape[1] // block_size)) * block_size
                x2 = (j % (mag.shape[1] // block_size)) * block_size
                y2 = (j // (mag.shape[1] // block_size)) * block_size
                cv2.rectangle(image, (x1, y1), (x1 + block_size, y1 + block_size), (0, 0, 255), 2)
                cv2.rectangle(image, (x2, y2), (x2 + block_size, y2 + block_size), (0, 0, 255), 2)

    return image
