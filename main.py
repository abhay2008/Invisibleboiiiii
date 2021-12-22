import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)
time.sleep(2)

bg = 0
for i in range(60):
  ret, bg = cap.read()

while (cap.isOpened()):
  ret, img = cap.read()
  if not ret:
    print('broken lol')
    break
  np.flip(img, axis=1)
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  lower_black = np.array([30, 30, 0])
  upper_black = np.array([104, 153, 0])
  mask1 = cv2.inRange(hsv, lower_black, upper_black)
  lower_black = np.array([60, 60, 0])
  upper_black = np.array([145, 178, 0])
  mask2 = cv2.inRange(hsv, lower_black, upper_black)
  mask1 = mask1 + mask2
  mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
  mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
  mask2 = cv2.bitwise_not(mask1)
  res1 = cv2.bitwise_and(img, img, mask=mask2)
  res2 = cv2.bitwise_and(bg, bg, mask=mask1)
  final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
  output.write(final_output)
  cv2.imshow('heya', final_output)
  cv2.waitKey(1)
  
cap.release()
out.release()
cv2.destroyAllWindows()
