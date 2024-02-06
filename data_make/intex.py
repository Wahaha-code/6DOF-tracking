from PIL import Image
import os

# 源文件夹和输出文件夹的路径
source_folder = 'data8/masks'
output_folder = 'data8/ba_masks'

# 如果输出文件夹不存在，就创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 仅处理PNG或JPG文件
    if filename.lower().endswith(('.png', '.jpg')):
        img_path = os.path.join(source_folder, filename)
        img = Image.open(img_path)

        # 转换为灰度图像
        img = img.convert('L')

        # 将所有非黑色像素设置为白色
        
        img = img.point(lambda p: 255 if p != 0 else 0)

        # 保存修改后的图像
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print("所有图像处理完成。")