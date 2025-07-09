import zipfile
import os

data_dir = "data"    # update based on current working directory

for file in os.listdir(data_dir):
    if(file.endswith(".zip")):
        zip_path = os.path.join(data_dir, file)
        extract_folder = os.path.join(data_dir, file.replace(".zip", ""))

        os.makedirs(extract_folder, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_reader:
            zip_reader.extractall(extract_folder)
