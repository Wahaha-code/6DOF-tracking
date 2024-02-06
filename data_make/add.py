import numpy as np
import inout  # 假设这是一个包含load_ply函数的模块

def transform_pts_Rt(pts, R, t):
    """Applies a rigid transformation to 3D points.

    :param pts: nx3 ndarray with 3D points.
    :param R: 3x3 rotation matrix.
    :param t: 3x1 translation vector.
    :return: nx3 ndarray with transformed 3D points.
    """
    assert pts.shape[1] == 3
    pts_t = R.dot(pts.T) + t.reshape((3, 1))
    return pts_t.T

def add(R_est, t_est, R_gt, t_gt, pts):
    """Average Distance of Model Points for objects with no indistinguishable views - by Hinterstoisser et al. (ACCV'12).
    :param R_est: 3x3 ndarray with the estimated rotation matrix.
    :param t_est: 3x1 ndarray with the estimated translation vector.
    :param R_gt: 3x3 ndarray with the ground-truth rotation matrix.
    :param t_gt: 3x1 ndarray with the ground-truth translation vector.
    :param pts: nx3 ndarray with 3D model points.
    :return: The calculated error.
    """
    pts_est = transform_pts_Rt(pts, R_est, t_est)
    pts_gt = transform_pts_Rt(pts, R_gt, t_gt)
    e = np.linalg.norm(pts_est - pts_gt, axis=1).mean()
    return e

if __name__ == "__main__":
    ply_model_paths = [str('/media/sunh/Samsung_T5/6D_data/my_6d/6D_PanelPose/work_space/data/model_data/panel2.ply')]
    model_ply = inout.load_ply(ply_model_paths[0])

    # 假设这些是你的输入值
    icp_result = np.eye(4)
    RT = np.eye(4)

    e = add(icp_result[:3, :3], icp_result[0:3, 3] * 1000, RT[:3, :3], RT[0:3, 3], model_ply)
    print("Average Distance Error:", e)