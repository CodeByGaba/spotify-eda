import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


"""
Data Understanding & Cleaning
- Loaded Spotify user data
- Checked the first 10 rows to understand structure
- Verified number of rows and columns
- Checked column names and data types
- Checked for missing values
- Count of churn vs active values
- Visualise churn
- Save cleaned dataset
"""

df= pd.read_csv("C:\\Users\\tshol\\Downloads\\spotify-eda-main\\spotify_churn_dataset.csv")

df.head(10)
df.shape
df.columns
df.info()

missing_values=df.isnull().sum()
print("missing values: ",missing_values)

churn_counts=df["churned"].value_counts()
print(churn_counts)

plt.figure(figsize=(6,4))
plt.savefig("graph.png")
sns.countplot(x='churned', data=df)
plt.title('Churned vs Active Users')
plt.xlabel('Churned (1 = Yes, 0 = No)')
plt.ylabel('Number of Users')
plt.show()

df.to_csv("spotify_dataset_clean.csv", index=False)