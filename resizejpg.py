import os
from PIL import Image
import glob
from tqdm import tqdm

def compress_jpg(input_path, quality=80):
    """
    压缩单个JPG文件
    :param input_path: 输入文件路径
    :param quality: 压缩质量（1-100）
    """
    try:
        # 打开图片
        img = Image.open(input_path)
        # 获取原始文件大小
        original_size = os.path.getsize(input_path)
        
        # 创建临时文件名
        directory = os.path.dirname(input_path)
        filename = os.path.basename(input_path)
        temp_path = os.path.join(directory, f"temp_{filename}")
        
        # 保存压缩后的图片
        img.save(temp_path, 'JPEG', quality=quality, optimize=True)
        
        # 获取压缩后的文件大小
        compressed_size = os.path.getsize(temp_path)
        
        # 如果压缩后的文件更小，则替换原文件
        if compressed_size < original_size:
            os.replace(temp_path, input_path)
            print(f"成功压缩 {input_path}")
            print(f"原始大小: {original_size/1024:.2f}KB")
            print(f"压缩后大小: {compressed_size/1024:.2f}KB")
            print(f"压缩率: {(1 - compressed_size/original_size)*100:.2f}%\n")
        else:
            os.remove(temp_path)
            print(f"跳过 {input_path} (压缩后文件更大)")
            
    except Exception as e:
        print(f"处理 {input_path} 时出错: {str(e)}")

def compress_all_jpg_in_directory(root_dir):
    """
    递归压缩目录下所有的JPG文件
    :param root_dir: 根目录路径
    """
    # 获取所有jpg文件（不区分大小写）
    jpg_files = []
    for ext in ('*.jpg', '*.jpeg', '*.JPG', '*.JPEG'):
        jpg_files.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))
    
    if not jpg_files:
        print("未找到JPG文件")
        return
    
    print(f"找到 {len(jpg_files)} 个JPG文件")
    
    # 压缩每个文件
    for jpg_file in tqdm(jpg_files, desc="compressing"):
        compress_jpg(jpg_file)


if __name__ == "__main__":
    compress_all_jpg_in_directory(".")
