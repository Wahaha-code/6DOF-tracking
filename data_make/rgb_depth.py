import pyrealsense2 as rs
import numpy as np
import cv2
import time
import os

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = pipeline.start(config)

depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: ", depth_scale)

align_to = rs.stream.color
align = rs.align(align_to)

# 创建保存图像的目录
save_path = os.path.join(os.getcwd(), "out", time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
os.makedirs(save_path, exist_ok=True)
os.makedirs(os.path.join(save_path, "color"), exist_ok=True)
os.makedirs(os.path.join(save_path, "depth"), exist_ok=True)

# 其它代码保持不变

frame_count = 0  # 初始化帧计数器

try:
    while True:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)

        aligned_depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        if not aligned_depth_frame or not color_frame:
            continue

        # 获取深度帧的数据，并确保数据类型为uint16
        depth_image = np.asanyarray(aligned_depth_frame.get_data(), dtype=np.uint16)
        color_image = np.asanyarray(color_frame.get_data())

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # 保存图像
        color_img_filename = os.path.join(save_path, "color", f"{frame_count}.png")
        depth_img_filename = os.path.join(save_path, "depth", f"{frame_count}.png")

        cv2.imwrite(color_img_filename, color_image)  # 保存彩色图像
        cv2.imwrite(depth_img_filename, depth_image)  # 保存深度图像，格式为uint16

        # 显示实时和保存后的图像
        cv2.imshow("live", np.hstack((color_image, depth_colormap)))

        # 'q' to quit
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break

        frame_count += 1  # 更新帧计数器

finally:
    pipeline.stop()