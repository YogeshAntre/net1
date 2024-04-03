from enum import Enum
class MongoConfig(Enum):
    mongo_host = "localhost"
    mongo_port = 27017
    mongo_db_name = "My_DB"
    mongo_backup_dir = "D:/mongo_backup_folder"