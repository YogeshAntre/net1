import shutil
import os
import datetime
from  folder_config import *
def backup_folder(source_folder, destination_folder):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name = os.path.basename(source_folder) + '_' + timestamp
    backup_folder_path = os.path.join(destination_folder, backup_folder_name)

    try:
        shutil.copytree(source_folder, backup_folder_path)
        print(f"Backup created successfully at: {backup_folder_path}")
    except Exception as e:
        print(f"Error occurred while creating backup: {e}")

#if __name__ == "__main__":
    #source_folder = "/path/to/source/folder"
    #destination_folder = "/path/to/destination/folder"
source_folder =FolderConfig.source_folder.value
destination_folder = FolderConfig.destination_folder.value

backup_folder(source_folder, destination_folder)
