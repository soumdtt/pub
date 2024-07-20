import cv2

# read the image
coke_img = cv2.imread("images/coca-cola-logo.png")

# use OpenCV  imshow(), display until we press any key
window = cv2.namedWindow("image")
cv2.imshow(window, coke_img)
# wait for a key press
cv2.waitKey(0)
# destroy the window
cv2.destroyWindow(window)