import pandas as pd
import numpy as np
from datetime import datetime
from prefect import task,flow

## load the extracted data:
@task
def load_extracted_data(df:pd.DataFrame)->pd.DataFrame:
    """
    """
    df=pd.read_csv("data/extracted_data.csv")

    return df


## transform by adding the unique userId and datetime
@task 
def add_unique_userId(df:pd.DataFrame)->pd.DataFrame:
    """
    """
    df['userId']=np.arange(1,len(df)+1)

@task 
def add_datetime(df:pd.DataFrame)->pd.DataFrame:
    """
    """
    df['datetime']=datetime.now()

@task
def save_transformed_data(df:pd.DataFrame):
    ## save the transformed data:
    df.to_csv("data/transformed_df.csv",index=False)

@flow
def transformation_workflow():
    """
    """
    extracted_df=load_extracted_data()

    transformed_df=add_unique_userId(df=extracted_df)

    transformed_df=add_datetime(df=transformed_df)

    save_transformed_data(df=transformed_df)


if __name__=="__main__":
    transformation_workflow()

    
