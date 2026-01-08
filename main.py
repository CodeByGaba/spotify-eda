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
- Visualize churn
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
#Insight: Churned users spend way less time listening per day

"""
Engagement Analysis: Listening Time vs Subscription Type 
-Compared average daily listening time between FREE and PREMIUM users
-Assessed whether paid users show higher engagement
-Used a boxplot to visualise differences in listening behavior
-Identified engagement patterns that may influence churn
"""
plt.figure()
df.boxplot(column="avg_daily_minutes", by="subscription_type")
plt.title("Listening Time by Subscription Type")
plt.suptitle("")
plt.xlabel("Subscription Type")
plt.ylabel("Average Daily Minutes")
plt.savefig("images/listening_time_by_subscription.png")
plt.close()
#Insight: Premium users listen more than free users, suggestion that paying users are more engaged and less likely to churn.



"""
Engagement Analysis: Playlists vs Listening Time
-Examined the relationship between number of playlists and listening time
-Used playlists as a proxy for personalization and user investment
-Visualized engagement differences using a boxplot
-Observed how higher personalization relates to stronger engagement
"""
plt.figure()
df.boxplot(column="avg_daily_minutes", by="number_of_playlists")
plt.title("Listening Time by Number of Playlists")
plt.suptitle("")
plt.xlabel('Number of Playlists')
plt.ylabel("Average Daily Minutes")
plt.savefig("images/listening_time_by_playlists.png")
plt.close()
#Insight: Users who create more playlists tend to listen more, indicating stronger engagement and retention.


"""
Engagement Analysis: Skips vs Listening Time
-Analyzed how skipping behavior relates to listening time
-Used skips per day as an indicator of content dissatisfaction
-Visualized engagement differences across skip levels
-Identified behavioral patterns associated with potential churn
"""
plt.figure()
df.boxplot(column="avg_daily_minutes", by="skips_per_day")
plt.title("Listening Time by Skips Per Day")
plt.suptitle("")
plt.xlabel("Skips Per Day")
plt.ylabel("Average Daily Minutes")
plt.savefig("images/listening_time_by_skips.png")
plt.close()
#Insight: Users who skip songs frequently spend less time listening overall, showing lower engagement.


"""
Engagement Analysis: Genre vs Engagement
-Compared average listening time across top music genres
-Evaluated whether certain genres drive higher user engagement
-Used a bar chart to highlight genre-based engagement differences
-Identified content categories with stronger retention potential
"""
plt.figure()
df.groupby("top_genre")["avg_daily_minutes"].mean().sort_values().plot(kind="bar")
plt.title("Average Listening Time by Top Genre")
plt.xlabel("Genre")
plt.ylabel("Average Daily Minutes")
plt.tight_layout()
plt.savefig("images/listening_time_genre.png")
plt.close()
#Insight: Some genres have higher listening time, showing content preference affects engagement.


"""
Churn Analysis: Listening Time vs Churn
- Compared listening time between churned and active users
- Assessed whether lower engagement is linked to churn
- Used a boxplot to visualize differences
"""
plt.figure()
df.boxplot(column="avg_daily_minutes", by="churned")
plt.title("Listening Time by Churn Status")
plt.suptitle("")
plt.xlabel("Churned (0 = Active, 1 = Churned)")
plt.ylabel("Average Daily Minutes")
plt.savefig("images/listening_time_by_churn.png")
plt.close()
#Insight: Churned users listen significantly less than active users.

"""
Churn Analysis: Subscription Type vs Churn
- Analyzed churn distribution across free and premium users
- Identified which subscription type is more likely to churn
"""
plt.figure()
pd.crosstab(df["subscription_type"], df["churned"]).plot(kind="bar")
plt.title("Churn by Subscription Type")
plt.xlabel("Subscription Type")
plt.ylabel("User Count")
plt.tight_layout()
plt.savefig("images/churn_by_subscription.png")
plt.close()
#Insight: Free users churn more often than premium users.


"""
Churn Analysis: Skips vs Churn
- Compared skipping behavior between churned and active users
- Used skips as a proxy for dissatisfaction
"""
plt.figure()
df.boxplot(column="skips_per_day", by="churned")
plt.title("Skips per Day by Churn Status")
plt.suptitle("")
plt.xlabel("Churned (0 = Active, 1 = Churned)")
plt.ylabel("Skips Per Day")
plt.savefig("images/skips_by_churn.png")
plt.close()
#Insight: Churned users skip more songs, indicating lower satisfaction.


"""
Churn Analysis: Playlists vs Churn
- Compared playlist creation between churned and active users
- Used playlists as a measure of user investment
"""
plt.figure()
df.boxplot(column="number_of_playlists", by="churned")
plt.title("Playlists by Churn Status")
plt.suptitle("")
plt.xlabel("Churned (0 = Active, 1 = Churned)")
plt.ylabel("Number of Playlists")
plt.savefig("images/playlists_by_churn.png")
plt.close()
#Insight: Users with fewer playlists are more likely to churn.










df.to_csv("spotify_dataset_clean.csv", index=False)
