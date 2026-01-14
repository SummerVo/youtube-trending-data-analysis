# YouTube Trending Data Analysis

## Overview
This project analyses **YouTube trending video data** to uncover patterns behind video popularity and engagement.  
It focuses on exploring **viewership trends, engagement metrics, and content categories** using an exploratory, visual analytics–driven approach.

The project is designed as a **data analytics portfolio project**, demonstrating practical data cleaning, exploration, and insight generation using real-world social media data.

---

## Objectives
- Explore patterns in **YouTube trending videos**
- Analyse engagement metrics such as views, likes, and comments
- Identify trends across **video categories and publish timing**
- Use visualisation to support analytical insights

---

## Data
The dataset is query from Google API using the functions in **[youtube_api_functions.py](./youtube_api_functions.py)** and includes:
- Video metadata (title, channel, category)
- Publish time and trending date
- Engagement metrics (views, likes, comments)

Data cleaning and preprocessing were performed to handle missing values and ensure consistency.

---

## Methods
- Data cleaning and preprocessing  
- Exploratory data analysis (EDA)  
- Distribution and trend visualisation
- Class balancing
- Binary classification 
- Sentiment analysis  

---
## Key Insights
- Exploratory analysis enabled feature reduction, improving model focus and training efficiency
- Model performance improved after addressing class imbalance in the dataset
- XGBoost achieved the best overall performance, while Naive Bayes predicted the highest number of correct trending videos
- Random Forest outperformed prior studies in accuracy and F1-score, highlighting dataset-dependent performance differences
- Feature importance analysis identified channel activity and publishing time as key predictors of trending videos:
      + channel_video_count
      + published_time
      + channelId
      + dayofweek
- Sentiment analysis using VADER (NLTK) found no significant difference in comment sentiment between trending and non-trending videos
---

## Tools
-
- Python libraries for EDA: pandas, NumPy, matplotlib, seaborn
- Jupyter Notebook for exploratory analysis
- SMOTE for class balancing
- Classification models: Random Forest, Logistic Regression, and Naive Bayes
- Vader for sentiment analysis
- googleapiclient for calling Google API 

---

## Output
- 📄 **[analyse_youtube_data.ipynb](./analyse_youtube_data.ipynb)** containing full analysis and visualisations

---

## Author
**Summer Vo**  
