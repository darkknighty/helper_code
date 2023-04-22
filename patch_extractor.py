import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image using OpenCV
img = cv2.imread("path/to/image.jpg")

# Read the coordinates from the CSV file
coords = np.loadtxt("path/to/coordinates.csv", delimiter=",")

# Loop through the coordinates and extract patches
for coord in coords:
    x, y = map(int, coord)
    left = x - 48
    top = y - 48
    patch = img[top:top+96, left:left+96, :]
    plt.imshow(cv2.cvtColor(patch, cv2.COLOR_BGR2RGB))
    plt.show()
