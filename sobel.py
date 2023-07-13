import  cv2
import numpy  as np
from matplotlib import pyplot as plt
img=cv2.imread("hand.jpg",0)
sobel_x=cv2.Sobel(img,-1,1,0)
sobel_y=cv2.Sobel(img,-1,0,1)
compine_sobel_x_with_sobel_y=cv2.bitwise_or(sobel_x,sobel_y)
"""ععلشان نشيل ال noise الي في الخلفيه"""
sobel_x=np.uint8(np.absolute(sobel_x))
sobel_y=np.uint8(np.absolute(sobel_y))
compine_sobel_x_with_sobel_y=np.uint8(np.absolute(compine_sobel_x_with_sobel_y))
cv2.imshow("img",img)
cv2.imshow("sobel_x",sobel_x)
cv2.imshow("sobel_y",sobel_y)
cv2.imshow("all",compine_sobel_x_with_sobel_y)
cv2.imwrite("D:\projects\python_pycharm\Laplacian\sobel_x.jpg",sobel_x)
cv2.imwrite("D:\projects\python_pycharm\Laplacian\sobel_y.jpg",sobel_y)
cv2.imwrite("D:\projects\python_pycharm\Laplacian\compine_sobel_x_with_sobel_y.jpg",compine_sobel_x_with_sobel_y)
cv2.waitKey(0)
cv2.destroyWindow()