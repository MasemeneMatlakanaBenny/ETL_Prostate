
import pandas as pd
import great_expectations as gx
from great_expectations.expectations.expectation import ExpectationConfiguration
from great_expectations.core.batch import Batch
from typing import List,Union

def create_batch(df:pd.DataFrame)->Batch:
    """
    Docstring for create_batch
    """
    context=gx.get_context()

    ## create the dataframe source -pandas in this case:
    data_source=context.data_sources.add_pandas("pandas_df")

    ## create the dataframe asset from the data source:
    data_asset=data_source.add_dataframe_asset("dataframe_asset")

    ## create the dataframe batch:
    batch_definition=data_asset.add_batch_definition_whole_dataframe("data_batch")
    batch=batch_definition.get_batch(batch_parameters={"dataframe":df})

    return batch


## create the min expectations for a column:
def create_min_expectations(min_value:Union[int,float],
                            max_value:Union[int,float],
                            column_name:str)->ExpectationConfiguration:
    """
    Docstring for create_min_expectations
    
    :param min_value: Minimum value expected for the numeric column
    :type min_value: Union[int, float]
    :param max_value: Maximum value expected for the numeric column
    :type max_value: Union[int, float]
    :param column_name: Name of ghe column to perform expectations on
    :type column_name: str
    :return: expectation configuration
    :rtype: Any
    """

    expectation=gx.expectations.ExpectColumnMinToBeBetween(
        min_value=min_value,max_value=max_value,column=column_name
    )

    return expectation


## create the max expectations for a column:
def create_max_expectations(min_value:Union[int,float],
                            max_value:Union[int,float],
                            column_name:str)->ExpectationConfiguration:
    """
    Docstring for create_max_expectations
    
    :param min_value: Maximum value expected for the numeric column
    :type min_value: Union[int, float]
    :param max_value: Maximum value expected for the numeric column
    :type max_value: Union[int, float]
    :param column_name: Name of the column to perform expectations on
    :type column_name: str
    :return: expectation configuration
    :rtype: Any
    """

    expectation=gx.expectations.ExpectColumnMaxToBeBetween(
        min_value=min_value,max_value=max_value,column=column_name
    )

    return expectation

## create the categorical expectations:
def create_categorical_expectations(unique_values:List[str],
                                    column_name)->ExpectationConfiguration:
    """
    Docstring for create_categorical_expectations
    
    :param unique_values: uniqueor distinct values stored in the column name
    :type unique_values: List[str]
    :param column_name: name of the column
    :return: Description
    :rtype: ExpectationConfiguration
    """

    expectation=gx.expectations.ExpectColumnDistinctValuesToContainSet(
        value_set=unique_values,column=column_name
    )

    return expectation


## run expectations:
def validate_expectations(batch:Batch,
                          expectations:List[ExpectationConfiguration],
                          expectation_labels:List[str]
                          )->pd.DataFrame:
    """
    Docstring for validate_expectations
    
    :param expectations: Description
    :type expectations: List[ExpectationConfiguration]
    :param expectation_labels: Description
    :type expectation_labels: List[str]
    """

    ## create an empty list to store data quality checks results
    expectation_results=[]

    ## validate each expectation in expectations
    for expectation in expectation:
        validation=batch.validate(expectation)

        results=validation[0]  

        ## append the results of the quality checks
        expectation_results.append(results)

    ## store the validation results in a dataframe -> meta validation
    validation_results_df=pd.DataFrame({
        "expectations":expectation_labels,
        "results":expectation_results
    })

    return validation_results_df

def meta_validations(batch:Batch,column_name):
    """
    Docstring for meta_validations
    
    :param batch: Description
    :type batch: Batch
    """
    
    ## create the expectation:
    expectation=gx.expectations.ExpectColumnDistinctValuesToEqualSet(
        value_set=["success"],column=column_name
    )

    results=batch.validate(expectation)[0]

    return results





