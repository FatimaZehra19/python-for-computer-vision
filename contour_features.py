import cv2
import numpy as np

image = cv2.imread("sample.jpg")

def rescaleFrame(frame,scale = 0.15):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale) 
    dimensions = (width,height)
    return cv2.resize(frame, dimensions)    


resized_image = rescaleFrame(image)

# Converting into Gray Scale 
gray_image = cv2.cvtColor( resized_image , cv2.COLOR_BGR2GRAY)

# Binary Threshold
_, thresh = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

# Creating Kernel 
kernel = np.ones((3,3),np.uint8) 

# Opening (Erosion then Dilation)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel)

# Contouring 
contours, hieararchy = cv2.findContours(opening , 
                                        cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE) 

print("Total contours found:", len(contours))

output = resized_image.copy()
cv2.drawContours(output, contours , -1, (0,255,0),4)


for cnt in contours:
    area = cv2.contourArea(cnt)
    print("Area:", area)
    x, y, w, h = cv2.boundingRect(cnt)
    
    if area > 80 :
        perimeter = cv2.arcLength(cnt,True)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 4)
    else:
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 225, 0), 2)
        
    print("Bounding Rect:", x, y, w, h)

    


cv2.imshow("Detected Objects", output)

cv2.waitKey(0)
cv2.destroyAllWindows()

