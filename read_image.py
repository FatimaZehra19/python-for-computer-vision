import cv2 

image = cv2.imread("sample.jpg")
if image is None:
    print("Image is not Loaded")
else: 
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows
 
 