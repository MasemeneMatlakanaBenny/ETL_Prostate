## ETL For Prostate
This is a project that follows every other ETL structure that I've worked on.
However it should be noted that the difference when it comes to this one is the improved workflow and structure used.
As such it must be noted that there are validation pipelines and meta validation pipelines compared to the previous ones
Annotation types have been improved when it comes to creating the libraries for reproducibility of the workflow

---

### Step 1 - Extraction
In the extraction phase,SQLAlchemy and Pandas are used more frequently for the workflow.
The os library too is used to get the credentials from the .env library which is not part of the repo in this case for security purposes
After extracting the data ,we save it to the data folder 
 The extraction is found under the src folder 
 
 src/
phases/
extract.py 
---

## Step 2: Extraction Validatio
In the extraction validation, pandas and great_expectations are used for the entire workflow
After we extracted the raw data from the database ,we must ensure the accuracy ,hence we perform data quality checks in this case
With great_expectations ,we perform data quality checks
