import cv2

# Image Read
cv_img = cv2.imread('owl.jpg')
cv2.imshow("cv_img", cv_img)

# Create Black_img
black_img = cv_img * 0
# Create White_img
white_img = black_img + 255

# Create Red_img(Split ⇒ Marge)
# 黒画像のチャンネルを分離
blue_img_cb, green_img_cb, red_img_cb = cv2.split(black_img)  # all "0"
# 白画像のチャンネルを分離
blue_img_cw, green_img_cw, red_img_cw = cv2.split(white_img)  # all "255"
# 白画像の赤成分と黒画像の緑青成分を結合
red_img = cv2.merge((blue_img_cb, green_img_cb, red_img_cw))  # (b,g,r) = (0,0,255)
cv2.imshow("red_img", red_img)

cv2.waitKey(0) & 0xFF == ord('q')
