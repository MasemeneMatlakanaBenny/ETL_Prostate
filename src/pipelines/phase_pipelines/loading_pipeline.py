import pandas as pd
import os
import hopsworks
from hopsworks.project import Project
from dotenv import load_dotenv
from prefect import task,flow

## load .env file with the use of load_dotenv
load_dotenv()

## load the extracted data:
@task
def load_transformed_data(df:pd.DataFrame)->pd.DataFrame:
    """
    """
    df=pd.read_csv("data/transformed_data.csv")

    return df

@task
def get_hopsworks_project():
    """
    """
    ## get the credentials :

    project_name=os.getenv("PROJECT_NAME")
    api_key=os.getenv("API_KEY")

    ## log into hopsworks:
    project=hopsworks.login(
    project=project_name,
    api_key_value=api_key
    )


    return project

@task
def get_feature_store(project:Project):
    """
    """
    feature_store=project.get_feature_store()

    return feature_store

@task
def get_feature_group(feature_store):
    """
    """

    feature_group=feature_store.get_or_create_group(
        name="",
        version=1,
        description="",
        primary_key=['userId'],
        event=['datetime']
    )

    return feature_group


@task
def load_data_to_group(feature_group,df:pd.DataFrame):
    """
    """

    feature_group.insert(df,write_options={"wait_for_job":False})

@flow
def load_workflow():
    """
    """

    ## load the transformed data
    df=load_transformed_data()

    ## get project  which allows us to login the lakehouse
    project=get_hopsworks_project()

    ## get the feature store:
    feature_store=get_feature_store(project=project)

    ## get the feature group
    feature_group=get_feature_group(feature_store=feature_store)

    ## load the data:
    load_data_to_group(feature_group=feature_group,df=df)

if __name__=="__main__":
    load_workflow()
    
