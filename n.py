import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("hotel bookings.csv")
df.shape
df.info()
df.isnull().sum()
df.drop(["company"],axis=1)
df.shape

median1=df["children"].median()
median()

df["children"].replace(np.nan,median1,inplace=True)
df.isnull().sum()

median2=df.["agent"].median()
median2()

df.["agent"].replace(np.nan,median2,inplace=True)
df.isnull().sum()


mode1=df["country"].mode().values[0]
model1
df.["country"].replace(np.nan,mode1,inplace=True)
df.isnull().sum()

duplicate=df.duplicated()
print(duplicate.sum())
df.drop_duplicated(inplace=True)
df.duplicated().sum()
df.shape
df.boxplot(column=["lead_time"])


def remove_outlier(col):
     sorted(col)
     Q1,Q3=col.quantile([0.25,0.75])
     IQR=Q3-Q1
     lower_range=Q1-1.5*IQR
     upper_range=Q3+1.5*IQR
     return lower_range,upper_range
     
low_leadtime,high_leadtime=remove_outlier(df["lead_time"]0
df["lead_time"]=np.where(df["lead_time"]>high_leadtime,high_lead_time,df["lead_time"])
df["lead_time"]=np.where(df["lead_time"]<high_leadtime,high_lead_time,df["lead_time"])

df.boxplot(column=["lead_time"])
df.shape

pd.get_dummies(df['hotel','arrival_date_month','meal','country','customer_type',deposit_type,'reserved_room_type','assigned_room_type','distribution_market','resevation_status_date')
dummies.head()

df=pd.concat([df,dummies],axis=1)
df

df.drop(columns,axis=1,inplace=True)
df

df.info()
 
df.dtypes
