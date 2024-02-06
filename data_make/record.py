import pyrealsense2 as rs
import cv2
import os
import time
import numpy as np

# 创建保存图像的文件夹
color_output_folder = 'data8/color'
depth_output_folder = 'data8/depth'
os.makedirs(color_output_folder, exist_ok=True)
os.makedirs(depth_output_folder, exist_ok=True)

# 相机配置
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
profile = pipeline.start(config)

# 创建对齐对象
align_to = rs.stream.color
align = rs.align(align_to)

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   Start Detection >>>>>>>>>>>>>>>>>>>>>>>>>>>>')
start_time = time.time()
frame_count = 0
while True:
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)
    aligned_depth_frame = aligned_frames.get_depth_frame()
    color_frame = aligned_frames.get_color_frame()
    depth_image = np.asanyarray(aligned_depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())

    # 生成文件名
    frame_number = frame_count + 1
    filename = f'{frame_number:04d}.png'
    color_file_path = os.path.join(color_output_folder, filename)
    depth_file_path = os.path.join(depth_output_folder, filename)

    # 保存颜色图像和深度图像
    cv2.imwrite(color_file_path, color_image)
    cv2.imwrite(depth_file_path, depth_image)

    cv2.imshow('Color Image', color_image)

    frame_count += 1

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) == ord('q') or time.time() - start_time > 30:
        break

# 关闭窗口并停止相机
cv2.destroyAllWindows()
pipeline.stop()

print(f'Total frames captured: {frame_count}')