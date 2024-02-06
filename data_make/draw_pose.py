import os
import cv2
import numpy as np

def create_coor(img, pose, intrinsic_matrix):
    # 函数的实现代码
    x_color = (255, 0, 0)
    y_color = (0, 255, 0)
    z_color = (0, 0, 255)
    corners_3D = np.array([[0, 0, 0],
                           [100, 0, 0],
                           [0, 100, 0],
                           [0, 0, 100]])

    ones = np.ones((corners_3D.shape[0], 1))
    homogenous_coordinate = np.append(corners_3D, ones, axis=1)

    homogenous_2D = intrinsic_matrix @ (pose @ homogenous_coordinate.T)
    coord_2D = homogenous_2D[:2, :] / homogenous_2D[2, :]
    coord_2D = ((np.floor(coord_2D)).T).astype(int)

    img = cv2.line(img, tuple(coord_2D[0]), tuple(coord_2D[1]), x_color, 5)
    img = cv2.line(img, tuple(coord_2D[0]), tuple(coord_2D[2]), y_color, 5)
    img = cv2.line(img, tuple(coord_2D[0]), tuple(coord_2D[3]), z_color, 5)

    return img

def main():
    # 定义相机位姿矩阵 pose
    pose = np.array([[1, -0, -0, -61.56289577],
                     [-0, 1, 0, 36.20676696],
                     [-0, -0, 1, 542.6501036]])

    # 定义相机内参矩阵 intrinsic_matrix
    intrinsic_matrix = np.array([[386.668457, 0, 327.455078],
                                 [0, 385.630249, 241.625610],
                                 [0, 0, 1]])

    # 指定图像目录路径
    image = '/home/guo/project/data_make/30.png'

    # 读取图像
    img = cv2.imread(image)
    
    # 调用 create_coor 函数绘制坐标系
    result = create_coor(img, pose, intrinsic_matrix)
    
    # 保存结果图像
    output_path = '/home/guo/project/data_make/result.png'
    cv2.imwrite(output_path, result)

if __name__ == '__main__':
    main()