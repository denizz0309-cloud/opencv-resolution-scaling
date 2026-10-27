import os
import sys

# OpenCV CUDA DLL paths
os.add_dll_directory(
    r"C:\Users\deniz\Downloads\opencv-build\bin\Release"
)

os.add_dll_directory(
    r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\bin"
)

# Custom CUDA-enabled OpenCV Python module
sys.path.insert(
    0,
    r"C:\Users\deniz\Downloads\opencv-build\lib\python3\Release"
)

import cv2

# Read image
image = cv2.imread("checkerboard.jpeg")

if image is None:
    print("Image not found!")
    sys.exit()

# Original resolution
height, width = image.shape[:2]

print("Original resolution:", width, "x", height)

# Required scales
scales = [2, 4, 0.5, 0.25]

for scale in scales:

    # Calculate new resolution
    new_width = int(width * scale)
    new_height = int(height * scale)

    # Resize image
    resized = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_LINEAR
    )

    # Create window
    window_name = f"Scale x{scale}"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Show image
    cv2.imshow(window_name, resized)

print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()