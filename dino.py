#As of now this script captures data from screen that can be customized by the user, and uses image annotation to display the pixel value that the user is interested in to the screen.
#Day/Night detection added. This will help later for the cactus-detection system.
#Image Manipulation-Related Functions

import cv2
import pyautogui
import numpy as np
#Image Manipulation Functions
def threshold(v1, v2, region):
    screenshot = pyautogui.screenshot(region = region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    (thresh, src) = cv2.threshold(screenshot,v1,v2,cv2.THRESH_BINARY)
    return (thresh,src)
def display_pixel_value(img,alt_img:None,text_pos, pixel, color):
    if alt_img is None:
        cv2.putText(img,str(img[pixel[0],pixel[1]]),(text_pos[0], text_pos[1]), cv2.FONT_HERSHEY_PLAIN, 2, (color[0], color[1], color[2]), 2)
    else:
        cv2.putText(img,str(alt_img[pixel[0],pixel[1]]),(text_pos[0], text_pos[1]), cv2.FONT_HERSHEY_PLAIN, 2, (color[0], color[1], color[2]), 2)

while True:
    #Thesholded Image
    img = threshold(127,255,(51,226,375,202))[1]
    # print(get_time(img, 0, 374))
    cv2.imshow("Capture:", img) 

    #UI Image
    graphic_img = pyautogui.screenshot(region = (51,226,375,202))
    graphic_img = np.array(graphic_img)

    cv2.line(graphic_img,(93,0),(93,149), (0,0,225), 2)
    display_pixel_value(graphic_img,img,(0,200),(151,80), (225, 0,0))
    cv2.imshow("Colored Capture:", graphic_img)

    

    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break

