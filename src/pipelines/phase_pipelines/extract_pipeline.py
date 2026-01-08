import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from prefect import task,flow

## load .env file with load_dotenv function:
load_dotenv()


@task
def create_connection_engine():
    """
    """
    user=os.getenv("USER")
    password=os.getenv("PASSWORD")
    schema_name=os.getenv("SCHEMA_NAME")


    ## create the engine with the use of sqlalchemy:
    engine=create_engine(f"mysql+pymysql://{user}:{password}@127.0.0.1:3306/{schema_name}")

    return engine


@task
def extract_data(engine:create_engine,db_name)->pd.DataFrame:
    """
    """
    # create the query now:
    query=f"""
        SELECT * 
         FROM {db_name}
        """
    ## get the query results and store them in dataframe 
    df=pd.read_sql_query(sql=query,con=engine)

    return df


## save the df to csv file:
@task
def save_extracted_data(df:pd.DataFrame):
    df.to_csv("data/extracted_data.csv",index=False)

@flow
def extraction_workflow():
    engine=create_connection_engine()

    db_name=os.getenv("DB_NAME")
    extracted_df=extract_data(engine=engine,db_name=db_name)

    save_extracted_data(df=extracted_df)

if __name__=="__main__":
    extraction_workflow()
    

