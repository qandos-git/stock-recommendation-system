# stock-recommendation-system
A machine learning-based system that provides stock recommendations based on Sentiment Analysis of stock news. This project leverages data preprocessing, feature engineering, and predictive modeling to suggest potential stocks for investment.


## Get the dataset


```
import kagglehub
path = kagglehub.dataset_download("myrios/news-sentiment-analysis", local_dir="sec/data/")

print("Path to dataset files:", path)
```