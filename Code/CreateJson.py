import os
from Preprocess import processing_data

# Directory containing xlsx files
dir_path = "E:/tugas_koko/Mencari_Kerja/Kerjaan/Paw_Patrol/Development/Data"

# List of xlsx file names in the directory
file_names = os.listdir(dir_path)

# Process each file
for file_name in file_names:
    if file_name.endswith(".xlsx"):
        file_path = os.path.join(dir_path, file_name)
        datafr = processing_data(file_path)