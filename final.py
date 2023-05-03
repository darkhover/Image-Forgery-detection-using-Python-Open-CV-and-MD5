import tkinter as tk
import cv2
from tkinter import filedialog

from secondcode import copy_move_detection

def detect_forgery():
    # Open a file dialog to select an image file.
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load the image file using OpenCV.
        image = cv2.imread(file_path)

        # Perform copy-move forgery detection using OpenCV.
        # Your code for this function can be the same as the one I provided in my previous answer.
        forgery_detection_image = copy_move_detection(image)

        # Display the result in a new window.
        cv2.imshow('Forgery Detection Result', forgery_detection_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Create a Tkinter window with a button to trigger the forgery detection.
root = tk.Tk()
root.title('Image Forgery Detection')
label = tk.Label(root, text="Image Forgery detection")
button = tk.Button(root, text='Select Image', command=detect_forgery)
button.pack()
label.pack()
root.mainloop()
