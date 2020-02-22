import cv2

# Image Read
cv_img = cv2.imread('owl.jpg')
cv2.imshow("cv_img", cv_img)

# Create Black_img
black_img = cv_img * 0
# Create White_img
white_img = black_img + 255
cv2.imshow("white_img", white_img)

cv2.waitKey(0) & 0xFF == ord('q')
