import cv2

# Image Read
cv_img = cv2.imread('owl.jpg')
cv2.imshow("cv_img", cv_img)

# Create Black_img
black_img = cv_img * 0
# Create White_img
white_img = black_img + 255

# Create gray_img(overlay)
# 黒/白の両画像に0.5の重みをかけて結合(オーバーレイ)
gray_img = cv2.addWeighted(black_img, 0.5, white_img, 0.5, 0)
cv2.imshow("gray_img", gray_img)

cv2.waitKey(0) & 0xFF == ord('q')
