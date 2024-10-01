import os
import cv2

img = cv2.imread('I:/Python/pythonProject/selfDigits/test1.png')
target_img = cv2.resize(img, (32, 32))
cv2.imwrite('I:/Python/pythonProject/selfDigitsNew/test1New.png', target_img)