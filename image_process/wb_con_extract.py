import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from colors import get_bg_color, get_text_color

# img = cv2.imread('/Users/skattish/Downloads/wb.jpg')
kernel5 = np.ones((5, 5), dtype = np.uint8)
kernel2 = np.ones((2, 2), dtype = np.uint8)
kernel3 = np.ones((3, 3), dtype = np.uint8)
# img2 = cv2.imread('/Users/skattish/Documents/image_process/dont_copy.jpeg')
def extract_wb_content(img):
	hh, ww, cc = img.shape

	# convert to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Background Color
	bk_color = get_bg_color()[0]

	#Text Color
	txt_color = get_text_color()[0]

	img_blur = cv2.GaussianBlur(gray, (5,5), 0)
	morphed_img = cv2.morphologyEx(img_blur, cv2.MORPH_OPEN, kernel2)
	thresh_img = cv2.adaptiveThreshold(morphed_img, 255, \
		cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,10)

	white_bg = np.full((hh, ww, cc), 255, dtype = np.uint8)
	mask_img = cv2.bitwise_or(white_bg, white_bg, mask = thresh_img)
	mask_img[mask_img[:].all(-1) == 0] = txt_color
	mask_img[np.all(mask_img == (255, 255, 255), axis = -1)] = bk_color
	return mask_img
