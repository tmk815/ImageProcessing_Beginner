import cv2
import numpy as np

cv_img = cv2.imread('owl.jpg')
cv2.imshow("cv_img", cv_img)

# Kernel for Shape
k = 0.3  # Shape Strength
shape_kernel = np.array([[0, -k, 0],
                         [-k, 1 + 4 * k, -k],
                         [0, -k, 0]])

shape_kernel2 = np.array([[-k, -k, -k],
                          [-k, 1 + (8 * k), -k],
                          [-k, -k, -k]])

shape_img_k = cv2.filter2D(cv_img, -1, shape_kernel)
shape_img_k2 = cv2.filter2D(cv_img, -1, shape_kernel2)
cv2.imshow("Shape Kernel1", shape_img_k)
cv2.imshow("Shape Kernel2", shape_img_k2)

cv2.waitKey(0) & 0xFF == ord('q')
