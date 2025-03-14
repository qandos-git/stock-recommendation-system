import yfinance as yf
from transformers import pipeline

class SentimentService():

    def __init__(self):
        self.pipeline = pipeline("text-classification", model="ProsusAI/finbert")

    async def get_ticker_news(self, ticker):
        '''
        Get the news for the given ticker
        '''
        print("Extract news of ticker",ticker)
        return yf.Ticker(ticker).get_news()

    async def analyze_sentiment(self, ticker):
        '''
        Analyze the sentiment of the news
        '''
        news = []
        news_list = await self.get_ticker_news(ticker)
        for article in news_list:
            publish_data = article['content']['pubDate']
            article_summary = article['content']['summary']
            news.append({'Date':f'{publish_data}',
                            'Article summary':f'{article_summary}',
                            'sentiment_score':f'{self.pipeline(article_summary)[0]["score"]}',
                            'Sentiment_label':f'{self.pipeline(article_summary)[0]["label"]}'})
        return news


