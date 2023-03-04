import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/HHE_14th-Aug//main/loan_prediction.csv")

df.head()
     
df.dtypes

sns.relplot(x="Views",y="Upvotes",data=df)

sns.relplot(x="Views" , y="Upvotes" , hue="tag" , data=df)

sns.catplot(x="education",y="avg_training_score",data=df)

sns.catplot(x="education",y="avg_training_score",jitter=false,data=df2)

sns.catplot(x="education",y="avg_training_score",hue="gender",data=df2)

sns.catplot(x="education",y="avg_training_score",kind="swarm",data=df2)

sns.catplot(x="education",y="avg_training_score",kind="box",data=df2)

sns.catplot(x="education",y="avg_training_score",hue="is_promoted,kind="violin",data=df2)
            
sns.catplot(x="education",y="avg_training_score",hue="is_promoted,kind="violin",data=df2)
     
sns.catplot(x="education",y="avg_training_score",hue="is_promoted,kind="violin",split=true,data=df2)

sns.catplot(x="education",y="avg_training_score",hue="is_promoted,kind="bar",data=df2)
          
sns.catplot(x="education",y="avg_training_score",hue="is_promoted,kind="point",data=df2)
           
