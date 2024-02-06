import pyrealsense2 as rs
import numpy as np
import os

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = pipeline.start(config)

depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: ", depth_scale)

# 获取相机内参矩阵
intrinsics = profile.get_stream(rs.stream.color).as_video_stream_profile().intrinsics

# 创建保存相机内参矩阵的文件
save_path = os.getcwd()
intrinsics_filename = os.path.join(save_path, "intrinsics.txt")

# 构建相机内参矩阵的NumPy数组
intrinsics_matrix = np.array([[intrinsics.fx, 0, intrinsics.ppx],
                              [0, intrinsics.fy, intrinsics.ppy],
                              [0, 0, 1]])

# 保存相机内参矩阵到文件
np.savetxt(intrinsics_filename, intrinsics_matrix, delimiter=',', fmt='%f')

print("Camera Intrinsics Matrix saved to:", intrinsics_filename)

pipeline.stop()