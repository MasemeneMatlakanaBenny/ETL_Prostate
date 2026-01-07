import pandas as pd
import numpy as np
from datetime import datetime

## load the extracted data:
df=pd.read_csv("data/extracted_data.csv")


## transform by adding the unique userId and datetime
df['userId']=np.arange(1,len(df)+1)
df['datetime']=datetime.now()

## save the transformed data:
df.to_csv("data/transformed_df.csv",index=False)
