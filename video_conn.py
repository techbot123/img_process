import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


cap = cv2.VideoCapture(0)


#callback function
def set_callback(event, x, y, flag, params):
	global center, click

	if event == cv2.EVENT_LBUTTONDOWN:
		if click:
			center = (x,y)
		else:
			click = True
			center = (x,y)




#define global variables
center = (0,0)
click = False


#cv2 connection to callback
cv2.namedWindow('test')
cv2.setMouseCallback('test', set_callback)

while True:
	ret, frame = cap.read()
	

	if click == True:
		cv2.circle(frame, center = center, radius = 15, thickness = 4, color = (255, 0,0))

	cv2.imshow('test', frame)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
