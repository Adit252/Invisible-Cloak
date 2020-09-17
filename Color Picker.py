import cv2
import numpy as np

#Setting up the webcam

wc = cv2.VideoCapture(0)
wc.open(0)
wc.set(3,640)       #width
wc.set(4,480)       #height
wc.set(10,150)

def empty(n):
    pass

#Creating a trackbar
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 640, 240)

cv2.createTrackbar('Hue min', 'Trackbars', 0, 179, empty)
cv2.createTrackbar('sat min', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('val min', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('Hue max', 'Trackbars', 179, 179, empty)
cv2.createTrackbar('sat max', 'Trackbars', 255, 255, empty)
cv2.createTrackbar('val max', 'Trackbars', 255, 255, empty)

#Reading the trackbar values

while(wc.isOpened()):
  # Capture frame-by-frame
  ret, img = wc.read()
  
  if ret == True:
    img = cv2.flip(img,1)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                       #hue saturation value model, make it easy to make color adjustments
    h_min = cv2.getTrackbarPos('Hue min', 'Trackbars')
    h_max = cv2.getTrackbarPos('Hue max', 'Trackbars')
    s_min = cv2.getTrackbarPos('sat min', 'Trackbars')
    s_max = cv2.getTrackbarPos('sat max', 'Trackbars')
    v_min = cv2.getTrackbarPos('val min', 'Trackbars')
    v_max = cv2.getTrackbarPos('val max', 'Trackbars')
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    #to get the color
    imgResult = cv2.bitwise_and(img, img, mask = mask)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    h_stack = np.hstack([img, mask, imgResult])
    
    cv2.imshow('Horizontal stacked', h_stack)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
  # Break the loop
  else: 
    break

# When everything done, release the video capture object
wc.release()
# Closes all the frames
cv2.destroyAllWindows()






    
    
