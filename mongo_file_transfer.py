# import os
# import datetime,time
# from pymongo import MongoClient
# import os
# import shutil
# import schedule
# def backup_mongodb_collections(host, port, db_name, dest_dir):
#     try:
#         client = MongoClient(host, port)
#         db = client[db_name]
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         backup_folder_name = db_name + '_backup_' + timestamp
#         backup_folder_path = os.path.join(dest_dir, backup_folder_name)
#         os.makedirs(backup_folder_path,exist_ok=True)
#         # all collections in the database
#         collections = db.list_collection_names()
#         # Backup each collection as a separate JSON file
#         for collection_name in collections:
#             collection_data = list(db[collection_name].find())
#             backup_file = os.path.join(backup_folder_path, f"{collection_name}.json")
#             with open(backup_file, "w") as f:
#                 f.write(str(collection_data))
#         print("MongoDB collections backup successful.")
#     except Exception as e:
#         print(f"Error occurred during MongoDB collections backup: {str(e)}")

# # Define source and destination directories for folder backup
# # source_folder = "/path/to/source/folder"
# # dest_folder = "/path/to/destination/folder"

# mongo_host = "localhost"
# mongo_port = 27017
# mongo_db_name = "My_DB"
# #mongo_db_name = "abg-finops"
# mongo_backup_dir ="D:/mongo_backup_folder"
# backup_mongodb_collections(mongo_host, mongo_port, mongo_db_name, mongo_backup_dir)

# #schedule.every().minutes.do(backup_mongodb_collections)
# schedule.every().minutes.at(":00").do(backup_mongodb_collections)

# # Main loop to keep the script running
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import datetime
import time
from pymongo import MongoClient
import os
import schedule
from mongo_config import *
def backup_mongodb_collections(host, port, db_name, dest_dir):
    try:
        client = MongoClient(host, port)
        db = client[db_name]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_folder_name = db_name + '_backup_' + timestamp
        backup_folder_path = os.path.join(dest_dir, backup_folder_name)
        os.makedirs(backup_folder_path, exist_ok=True)
        
        # All collections in the database
        collections = db.list_collection_names()
        
        # Backup each collection as a separate JSON file
        for collection_name in collections:
            collection_data = list(db[collection_name].find())
            backup_file = os.path.join(backup_folder_path, f"{collection_name}.json")
            with open(backup_file, "w") as f:
                f.write(str(collection_data))
                
        print("MongoDB collections backup successful.")
    except Exception as e:
        print(f"Error occurred during MongoDB collections backup: {str(e)}")

mongo_host = MongoConfig.mongo_host.value
mongo_port = MongoConfig.mongo_port.value
mongo_db_name = MongoConfig.mongo_db_name.value
mongo_backup_dir = MongoConfig.mongo_backup_dir.value

backup_mongodb_collections(mongo_host, mongo_port, mongo_db_name, mongo_backup_dir)

