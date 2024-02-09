import os
import shutil

# Define the source directory containing the files
src_dir = r'C:\Users\ADMIN\OneDrive\Desktop\Files\Data Science'

# Define the destination directory where the files will be moved to
dst_dir = 'URL_ID.txt files/'

# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Loop through each file and move it to the destination directory
for file in files:
    if file.endswith('.txt'):  # only move .txt files
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        shutil.move(src_path, dst_path)
