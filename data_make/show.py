import cv2
import numpy as np

# 读取深度图像
depth_image_path = r'E:\data\rongeur\depth\0001.png'
depth_image = cv2.imread(depth_image_path, cv2.IMREAD_UNCHANGED)

# 检查图像是否成功载入
if depth_image is None:
    raise ValueError("无法加载图像，请检查路径是否正确")

# 将深度图像转换为8位格式以用于显示
# 你可以通过更改alpha值来调整深度图像的可视化效果
depth_image_8bit = cv2.convertScaleAbs(depth_image, alpha=0.2) 

# 应用颜色映射
depth_colormap = cv2.applyColorMap(depth_image_8bit, cv2.COLORMAP_JET)

# 显示彩色映射的深度图像
cv2.imshow('Depth Image', depth_colormap)
cv2.waitKey(0)
cv2.destroyAllWindows()