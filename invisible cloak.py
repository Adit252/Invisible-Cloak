import numpy as np
import cv2
import time

wc = cv2.VideoCapture(0)
time.sleep(3)       # so that when it works efficiently from starting
bg = 0

for i in range(40):
    ret, bg = wc.read()    #capturing the background properly

while(wc.isOpened()):
    ret, image = wc.read()
    if ret == True:
        
        imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)        #converting it to hsv image 
        lower = np.array([125, 175, 25])                         #getting the hsv values using the color picker code of a particular color
        upper = np.array([179, 255, 255])                       #Put first three values of the trackbar in lower and last three in upper
        
        mask1 = cv2.inRange(imghsv, lower, upper)   #segmenting the image of the color part
        
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))   #dilating the mask so as to get a better view of that mask
     
        mask2 = cv2.bitwise_not(mask1)   #segmenting the part which is not colored
        
        result1 = cv2.bitwise_and(image, image, mask=mask2)  #the used cloth color will get replaced by black keeping rest same 
        result2 = cv2.bitwise_and(bg, bg, mask=mask1) # the used cloth color get replaced by the background
        
        finalOutput = cv2.addWeighted(result1, 1, result2, 1, 0) #It will add both the results and give the final output image
        
        cv2.imshow("magic", finalOutput)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else : break

wc.release()
cv2.destroyAllWindows()

    

