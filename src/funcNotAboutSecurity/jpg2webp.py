from PIL import Image

## 将一张png图片转化为webp

def convert_png_to_webp(input_path, output_path):
    # 打开PNG图片
    with Image.open(input_path) as img:
        # 将图像转换为RGB模式（WebP不支持RGBA）
        img = img.convert('RGB')
        # 保存为WebP格式
        img.save(output_path, 'webp')

# 示例用法
input_png = 'image.jpg'  # 输入的PNG文件路径
output_webp = 'output.webp'  # 输出的WebP文件路径
convert_png_to_webp(input_png, output_webp)

print(f"已将 {input_png} 转换为 {output_webp}")

