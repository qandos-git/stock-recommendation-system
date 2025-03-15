
# Stock Recommendation System
## Overview

This project builds an stock recommendation system, the system answers a widly asked question by investors, that is: which stock is better to invest in? 

To give you the answer, we built a recommendation system that gets list of stocks symbols from the user, then return them ranked from best to lowest. 

The stock news sentiment affects the stock price, as the invseteros actions affected by the news either by buying stocks that have good news (which lead to stock price increase) or selling stock that have bad news (which lead to stock price decrease). With this app you can estimate the feuture and making your investment decision based on ground truth.

I am planning to keep improving this project, help me with your ideas and your insights. 

## Features
- **Model-Controller-Service (MCS) Architecture**: Make this app maintainable and scaliable by seprating (Model): schema, from (Service) logic, from (Controller) the project core that links between models and services. This is a famous design pattern for API devlopment.

- **FastAPI**: RESTful API that process user input asycnorounsly.

- **Dockerized App**: Test this app by pulling the app image from docker hub.- 


## System main Components:


1. **SentimentService.py**: We used `yfinance` api to extract recent news of each ticker(stock), then we pass these news to [FinBERT model](https://huggingface.co/ProsusAI/finbert) a pre-trained NLP model to analyze sentiment of financial text. This module returns sentiment labeled news for each ticker.

3. **EvaluateService.py**: Compute the score of each ticker based on the average news sentiment of each ticker, the most positive ticker will get higher scores, whereas the least negative ticker will get lower scores.

5. **stock.py**: The main component of this app that handle the user input and call EvaluateService to do its job.

6. **InputValidator.py**: Ensure the user input a valid stock symbol, and the input at all is valid.


## Run the Stock Recommendation App from Docker Hub:

1.  If you don’t have Docker installed, follow the [Docker installation](https://docs.docker.com/engine/install/) guide for your operating system.

 
2. Pull and Run Docker Image in single command:
   
       run -d --name stock-rank-app-container -p 8000:8000 qandos/stock-ranker-app:latest
   
3. Example Request
To rank stocks based on sentiment analysis, use the POST endpoint /stock/v1/ with a JSON payload like this:

        {"symbols": ["AAPL", "TSLA", "GOOGL"]}

4. Use Post man from `src\assets\stock-ranker.postman_collection.json` or use CURL:

                curl -X 'POST' \
                'http://127.0.0.1:8001/stock/v1/' \
                -H 'Content-Type: application/json' \
                -d '{
                    "symbols": ["AAPL", "TSLA", "GOOGL"]
                }' 

### System Architecture
~soon

### Youtube Explanation in Arabic
~soon

## Resources
[FastAPI Backend Architecture: Model-Controller-Service](https://medium.com/@jeremyalvax/fastapi-backend-architecture-model-controller-service-44e920567699)

[How I code a Python Stock Screener & A.I. Sentiment Analysis to pick stocks.](https://medium.com/@chedy.smaoui/how-i-code-a-python-stock-screener-a-i-sentiment-analysis-to-pick-stocks-77059463f77a)


