import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Row and columns :{df.shape}")
    print(df.head())
    # converting csv data frame to json to insert int mangodb
    df.reset_index(drop=True,inplace=True)
    print(df.head())
    json_records=list(json.loads(df.T.to_json()).values())

    print(json_records[0])
    # inserting converted json record into mango db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)