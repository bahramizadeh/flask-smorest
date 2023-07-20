import requests
from flask import Flask


# from flask_smorest import Blueprint, Api



app = Flask(__name__)


@app.get("/markets/summaries")
def get_all_markets_summaries():
    response = requests.get("https://api.bittrex.com/v3/markets/summaries")
    return response.json()


@app.get("/markets/<string:marketSymbol>/summary")
def get_market_sammary(marketSymbol):
    response = requests.get(f"https://api.bittrex.com/v3/markets/{marketSymbol}/summary")
    return response.json()
