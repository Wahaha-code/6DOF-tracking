import cv2

# 读取深度图像
depth_image_path = 'E:/data/rgb/0002.png'
depth_image = cv2.imread(depth_image_path, cv2.IMREAD_UNCHANGED)

# 检查图像的数据类型
data_type = depth_image.dtype

print(f"图像的数据类型是：{data_type}")