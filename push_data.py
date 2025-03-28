import os
import sys
import json
from dotenv import load_dotenv
from pymongo.server_api import ServerApi

load_dotenv()
# Load environment variables from .env file
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi  # provides set of root certificates for SSL/TLS connections
ca  = certifi.where()

import pandas as pd
import numpy as np
from pymongo import MongoClient
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger 

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.T.to_json()
            records = json.loads(records).values()
            records = list(records) 
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database,collection):
        try:
            # Create a MongoDB client
            self.database=database
            self.collection=collection
            self.client = MongoClient(MONGO_DB_URL, server_api=ServerApi('1'))
            
            # Access the database and collection
            self.database = self.client[self.database]
            self.collection = self.database[self.collection]
            
            # Insert the records into the collection
            result = self.collection.insert_many(records)
            
            # Close the connection
            self.client.close()
            
            return result.inserted_ids
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="network_data\phisingData.csv"
    DATABASE="rajeshr"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)