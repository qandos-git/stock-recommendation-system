import pandas as pd
from .SentimentService import SentimentService
from models import WeightEnum, StockRequest


class EvaluateService():
    def __init__(self):
        self.analaizer = SentimentService()
        self.sentiment_weights = {"positive": WeightEnum.POSITIVE_NEWS.value,
                                  "neutral": WeightEnum.NEUTRAL_NEWS.value,
                                  "negative": WeightEnum.NEGATIVE_NEWS.value
                                  }

    async def evaluate(self, input):
        for ticker in input.keys():
            df = await self.analaizer.analyze_sentiment(ticker)
            df = pd.DataFrame(df)
            df['sentiment_weight'] = df['Sentiment_label'].map(self.sentiment_weights)
            df['sentiment_score'] = pd.to_numeric(df['sentiment_score'], errors='coerce')
            result = (df['sentiment_score'] * df['sentiment_weight']).sum()
            input[ticker] = result
        return input

    async def rank_stock(self, input:StockRequest):
        input_data = input.symbols
        input_data = {symbol: 0.0 for symbol in input_data}
        evaluated_stocks = await self.evaluate(input_data)
        return dict(sorted(evaluated_stocks.items(), key=lambda item: item[1], reverse=True))


