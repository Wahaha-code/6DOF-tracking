import cv2
import os
import glob

# PNG图像的原始文件夹路径
png_folder_path = r'data8/color'

# JPG图像要保存的文件夹路径
jpg_folder_path = r'data8/jpg'

# 如果JPG保存路径不存在，则创建
if not os.path.exists(jpg_folder_path):
    os.makedirs(jpg_folder_path)

# 遍历原始文件夹中的所有PNG图像
for png_file in glob.glob(os.path.join(png_folder_path, '*.png')):
    # 读取PNG图像
    img = cv2.imread(png_file)

    # 创建JPG版本的文件名
    jpg_file = os.path.splitext(os.path.basename(png_file))[0] + '.jpg'
    jpg_file_path = os.path.join(jpg_folder_path, jpg_file)

    # 保存为JPG格式
    cv2.imwrite(jpg_file_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

print("所有PNG图像已转换为JPG格式并保存至指定路径。")