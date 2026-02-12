# python-for-computer-vision
## 📌 Project Overview
This repository contains my foundational work in Computer Vision using Python and OpenCV.
It focuses on understanding how images are represented, accessed, and modified programmatically.

---

## 📅 Daily Progress

Day 1:
- Environment setup (VS Code, OpenCV)
- Read and display images
- First GitHub commit

Day 2:
- Understanding image shape and color channels
- Grayscale vs color images
- Pixel intensity values (0–255)

Day 3:
- Pixel access using array indexing
- Image slicing and ROI selection
- Rescaling images with custom functions

Day 4:
- Understanding BGR vs RGB color spaces
- Converting images to grayscale
- Learning why grayscale is used in computer vision

 Day 5:
- Understanding image noise
- Applying averaging and Gaussian blur
- Edge detection using Canny algorithm

Day 6:
- Understanding image thresholding
- Binary and adaptive thresholding
- Separating objects from background

Day 7:
- Morphological operations for binary image cleaning
- Erosion, dilation, opening, and closing

Day 8:
- Implemented contour detection using cv2.findContours()
- Detected object boundaries on binary images
- Used RETR_EXTERNAL to extract outer contours
- Applied CHAIN_APPROX_SIMPLE for contour compression
- Visualized contours using cv2.drawContours()
- Counted detected objects using len(contours)

Day 9:
- Extracted contour features (area and perimeter)
- Applied area-based filtering to remove small objects
- Drew bounding rectangles around detected objects
- Built structured mini object detection pipeline
---

## 🧠 Concepts Covered
- Reading and displaying images
- Images as NumPy arrays
- Image shape (height, width, channels)
- Pixel access and manipulation
- Image slicing and Region of Interest (ROI)
- Rescaling images using custom functions
- BGR to RBG conversion and gray scale images
- Image blurring and edge detection
- image thresholding (binary & adaptive)
- morphological operations: erosion, dilation, opening, closing
- contour detection with preprocessing (thresholding + morphology)
- contour feature extraction (area, perimeter, bounding box)

  
---

## 🛠 Technologies Used
- Python
- OpenCV
- NumPy

---

## 📂 Files Description
- read_image.py → Load and display images safely
- pixel_operations.py → Pixel access, slicing, and modification
- rescale_image.py → Custom function for resizing images
- thresholding.py → Global and adaptive thresholding examples
- morphology.py → Erosion, dilation, opening, and closing operations
- contours.py → Object boundary detection using findContours()


## 📈 Status
Actively expanding with daily learning and experiments.
