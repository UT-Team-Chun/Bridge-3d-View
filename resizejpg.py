import os
from PIL import Image
import glob
from tqdm import tqdm

def compress_jpg(input_path, quality=80):

    try:
        # open image
        img = Image.open(input_path)
        # get original file size
        original_size = os.path.getsize(input_path)
        
        # get file directory and name
        directory = os.path.dirname(input_path)
        filename = os.path.basename(input_path)
        temp_path = os.path.join(directory, f"temp_{filename}")
        
        # save compressed image to temp file
        img.save(temp_path, 'JPEG', quality=quality, optimize=True)
        
        # get compressed file size
        compressed_size = os.path.getsize(temp_path)
        
        # replace original file with compressed file if smaller
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

    # get all jpg files
    jpg_files = []
    for ext in ('*.jpg', '*.jpeg', '*.JPG', '*.JPEG'):
        jpg_files.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))
    
    if not jpg_files:
        print("未找到JPG文件")
        return
    
    print(f"找到 {len(jpg_files)} 个JPG文件")
    
    # compress jpg files
    for jpg_file in tqdm(jpg_files, desc="compressing"):
        compress_jpg(jpg_file)


if __name__ == "__main__":
    compress_all_jpg_in_directory(".")
