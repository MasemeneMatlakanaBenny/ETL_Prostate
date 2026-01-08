## ETL For Prostate
This is a project that follows every other ETL structure that I've worked on.
However it should be noted that the difference when it comes to this one is the improved workflow and structure used.
As such it must be noted that there are validation pipelines and meta validation pipelines compared to the previous ones
Annotation types have been improved when it comes to creating the libraries for reproducibility of the workflow

---

### ETL Phases:


#### Step 1 - Extraction
In the extraction phase,SQLAlchemy and Pandas are used more frequently for the workflow.
The os library too is used to get the credentials from the .env library which is not part of the repo in this case for security purposes
After extracting the data ,we save it to the data folder 
 The extraction is found under the src folder 
 
 src/
phases/
extract.py 



#### Step 2: Extraction Validation
In the extraction validation, pandas and great_expectations are used for the entire workflow
After we extracted the raw data from the database ,we must ensure the accuracy ,hence we perform data quality checks in this case
With great_expectations ,we perform data quality checks.
The extraction validation file is found in the src folder

src/
validations/
extract_vals.py


#### Step 3:Meta Extraction Validation

After performing data validations,we store the validation results in a dataframe in the data folder in a csv format.
From there,we perform validations for validation results,that is meta data validation. 
In other words,meta data validation is validation about validation,that is validating the validations themselves.
With great_expectations,we perform these meta data validation for the extraction phase for the file is located in the src folder

src/
validations/
meta_extract_vals.py



#### Step 4: Transformation
This is the second phase of the ETL pipeline. Here we transform the data ,check for missing values and ensure that we have clean data in the end.
As such ,each user must now have unique user_id which can be added using the numpy library and datetime. Those are the only two transformations performed.
The transformation file is found in the src folder

src/
phases/
transform.py

#### Step 5: loading
The last phase of the ETL pipeline which is loading the data into the lakehouse for future work. In this case,hopsworks which is a modern AI lakehouse is 
the one used for data storage or loading or final destination. We create the project in hopsworks which can then be used to create the feature store and feature views
to perform SQL operations over the data for future and consumption data workflow.
The loading file is found in the src folder:

src/
phases/
loading.py

-----
### Pipelines: 

Now building data pipelines with the use of the orchestration frameworks for scheduling of the workflow,notifications using webhooks and planning for failures.
In this case ,we rely on Prefect as the main orchestration framework. Other options such as Airflow,Kubeflow and Flytekit are available and can definitely suit the 
workflow. 
Using prefect ,we can perfectly set up webhooks for messages using APIs ,cache some of the task ,plan for failures and schedule the workflow.
Under prefect,we break down the phases that must be followed to execute the entire workflow into smaller components called tasks. 
From there,we then combine these tasks into a flow ,which is the sequence or order of how the tasks follow each other to get succcessful results.

The following are the pipelines of the workflow:

#### Extraction Pipeline:
The tasks for the extraction pipeline in which they will form the flow of the extraction pipeline. 
Create Engine using SQLAlchemy to connect to the database ->
Query & Extract the data ->
Save the extracted data.
The file for the pipeline :

src/pipelines/phase_pipelines/extract_pipeline.py

#### Extraction Validation Pipeline:
The tasks for the pipeline for validating the extracted data in which they will from the flow of the extraction validation pipeline.
Load the extracted data using Pandas ->
Create the data batch using the extracted data ->
Create the data quality checks to be performed ->
Test the data quality checks ->
Create the data quality checks results dataframe ->
Save it to the data folder in a csv format.

The file for the pipeline :

src/pipelines/validation_pipelines/extract_vals_pipeline.py

#### Meta Extraction Validation Pipeline:
The tasks for the pipeline for validating the validated results in which they will from the flow of the meta extraction validation pipeline.
As defined and well explained before,meta data validation is validating the validation results,that is validation about validation.
Get the data quality checks dataframe in a csv format using pandas ->
Create the meta data batch ->
Create the meta data quality checks to be performed -Expect "success" only which means all the data quality checks has been passed ->
Test the meta data quality checks->
If success -> all data quality checks has been passed.


The file for the pipeline :

src/pipelines/validation_pipelines/meta_extract_vals_pipeline.py

#### Transformation Pipeline:
The tasks for transformation pipeline in which they will form the flow of the transformation pipeline.
Get the extracted data using pandas->
add unique user id & datetime - this can performed in a synchronous manner ->
save the transformed data in the data folder in a csv format.


The file for the pipeline :

src/pipelines/phase_pipelines/transform_pipeline.py

#### Loading Pipeline :
The tasks for pipeline that are to be followed for a successful data loading workflow into the AI lakehouse.
Get the transformed data using pandas->
Get hopsworks project ->
Create the feature store ->
Create the feature group ->
Load the data into the feature group ->
Create the feature view (optional).


The file for the pipeline :

src/pipelines/phase_pipelines/loading_pipeline.py

--------





