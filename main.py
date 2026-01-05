import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


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
sns.countplot(x='churned', data=df)
plt.title('Churned vs Active Users')
plt.xlabel('Churned (1 = Yes, 0 = No)')
plt.ylabel('Number of Users')
plt.savefig("graph.png")
plt.show()

"""
Exploratory Data Analysis
-Compared churned vs non-churned users
-Analyze listening behavior
"""

df.groupby("churned").mean(numeric_only=True)
pd.crosstab(["subscription_type"], df["churned"])

#Avg daily minutes vs churn
#Churn distribution

os.makedirs("images", exist_ok=True)
plt.figure()
df["churned"].value_counts().plot(kind="bar")
plt.title('Churn Distribution')
plt.xlabel("Churned")
plt.ylabel("Number of Users")
plt.savefig("images/churn_distribution.png")
plt.close()

#listening time vs churn
plt.figure()
df.boxplot(column="avg_daily_minutes", by="churned")
plt.title("Listening Time vs Churn")
plt.suptitle("")
plt.savefig("images/listening_time_vs_churn.png")
plt.close()

"""
Insight:
Churned users spend way less time listening per day,
indicating lower engagement before churn.
"""

df.to_csv("spotify_dataset_clean.csv", index=False)