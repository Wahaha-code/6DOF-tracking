import os
import cv2

# 图片目录和输出视频路径
image_dir = 'pose_vis'
output_video = 'demo2.mp4'

# 获取图片列表
image_files = sorted([f for f in os.listdir(image_dir) if f.endswith('.png')])

# 获取第一张图片的尺寸
first_image_path = os.path.join(image_dir, image_files[0])
first_image = cv2.imread(first_image_path)
height, width, _ = first_image.shape

# 创建视频编写器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video, fourcc, 30.0, (width, height))

# 逐个读取图片并写入视频
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    image = cv2.imread(image_path)
    video_writer.write(image)

# 释放视频编写器
video_writer.release()