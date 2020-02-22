import cv2

cv_img = cv2.imread('owl.jpg')
cv2.imshow("cv_img", cv_img)

# Sobel Filter x
gray_img = cv2.imread('owl.jpg', 0) # input gray
sobel_img = cv2.Sobel(gray_img, cv2.CV_32F, 1, 0, ksize=3) # cv2.CV_32F
cv2.imshow("Sobel Kernel", sobel_img)

cv2.waitKey(0) & 0xFF == ord('q')