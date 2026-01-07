import pandas as pd
import os
import hopsworks
from dotenv import load_dotenv

## load .env file with the use of load_dotenv
load_dotenv()

## get the data first:
df=pd.read_csv("data/transformed_df.csv")


## get the credentials :
project_name=os.getenv("PROJECT_NAME")
api_key=os.getenv("API_KEY")


## log into hopsworks:
project=hopsworks.login(
    project=project_name,
    api_key_value=api_key
)

## get the feature store:
feature_store=project.get_feature_store()

## create the feature group:
feature_group=project.get_or_create_group(
    name="prostate_group",
    description="Prostate for Classification ML workflow",
    version=1,
    primary_key=['userId'],
    event=['datetime']
    )

## insert the data:
feature_group.insert(df,write_options={"wait_for_job":False})

