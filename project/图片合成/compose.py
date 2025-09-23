from PIL import Image

import os

currentPath = os.path.dirname(os.path.abspath(__file__))

# 获取当前路径下imgs中的所有图片路径
print(currentPath)
# for n in os.listdir(os.path.join(currentPath, 'imgs')):
#     print(n)

# 拿到第一张图片的地址
name_list = os.listdir(os.path.join(currentPath, "imgs"))
first_img_name = name_list[0]
first_img_path = os.path.join(currentPath, "imgs", first_img_name)
img = Image.open(first_img_path)
# 拿到第一张图片的高度和宽度
width, height = img.size
print(width, height)

# 开始合成图片
# 图片行数
image_row = 5
# 图片列数
image_col = 3

# 创建新的画布
new_img = Image.new("RGB", (image_col * width, image_row * height))

for x in range(image_row):  # 行
    for y in range(image_col):  # 列
        # 打开要合成的图片
        img_index = image_col * x + y
        print(img_index)
        temp_img = Image.open(os.path.join(currentPath, "imgs", name_list[img_index]))
        new_img.paste(temp_img, (y * width, x * height))
new_img.save(os.path.join(currentPath, "imgs", "合成新的图片.jpg"))
