from pymongo import MongoClient

import os
from dotenv import load_dotenv
#  load environment variables from .env file
load_dotenv()

# # # get environment variables
# # # MONGODB_URI = os.getenv('MONGODB_URI')
# # # print(MONGODB_URI)
MONGODB_URI= os.environ.get('MONGODB_URL')
print(MONGODB_URI)
DB_NAME = os.environ.get('DATABASE_NAME')
# COLLECTION_NAME = os.environ.get('COLLECTION_NAME')


client = MongoClient(MONGODB_URI)
db = client[DB_NAME]







# class My_Database:
#     def __init__(self,user_details):
#         self.user_details = user_details
#         self.client = MongoClient(MONGODB_URI) 
#         self.db = self.client[DB_NAME] 
#         self.collection=self.db[COLLECTION_NAME]

#     def insert_user(self):
        
#         self.collection.insert_one(self.user_details)

#     def get_collection(self, COLLECTION_NAME): 
#         return self.db[COLLECTION_NAME] 
    

# from pymongo import MongoClient

