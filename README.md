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

----

#### Step 2: Extraction Validation
In the extraction validation, pandas and great_expectations are used for the entire workflow
After we extracted the raw data from the database ,we must ensure the accuracy ,hence we perform data quality checks in this case
With great_expectations ,we perform data quality checks.
The extraction validation file is found in the src folder

src/
validations/
extract_vals.py

----

#### Step 3:Meta Extraction Validation

After performing data validations,we store the validation results in a dataframe in the data folder in a csv format.
From there,we perform validations for validation results,that is meta data validation. 
In other words,meta data validation is validation about validation,that is validating the validations themselves.
With great_expectations,we perform these meta data validation for the extraction phase for the file is located in the src folder

src/
validations/
meta_extract_vals.py

----

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

### Pipelines

