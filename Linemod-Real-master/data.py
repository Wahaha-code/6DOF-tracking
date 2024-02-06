import cv2

# 读取图像
image = cv2.imread('LINEMOD/5/data/01/mask/0000.png')

# 获取图像的尺寸
height, width = image.shape[:2]

# 输出图像的尺寸
print("图像宽度：", width)
print("图像高度：", height)