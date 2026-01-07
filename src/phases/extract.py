import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

## load .env file with load_dotenv function:
load_dotenv()

## get the credentials necessary to get started:
user=os.getenv("USER")
password=os.getenv("PASSWORD")

schema_name=os.getenv("SCHEMA_NAME")
db_name=os.getenv("DB_NAME")


## create the engine with the use of sqlalchemy:

engine=create_engine(f"mysql+pymysql://{user}:{password}@127.0.0.1:3306/{schema_name}")

## create the query now:
query=f"""
        SELECT * 
         FROM {db_name}
        """

## get the query results and store them in dataframe 
df=pd.read_sql_query(sql=query,con=engine)

## save the df to csv file:
df.to_csv("data/extracted_data.csv",index=False)



