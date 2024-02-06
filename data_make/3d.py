import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 设置图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = np.load('img.pkl', allow_pickle=True)
# 获取顶点坐标数组
vertices = data['orientation_in_body']

# 提取 x、y、z 坐标
x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

# 绘制散点图
ax.scatter(x, y, z)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()