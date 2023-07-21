import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from schemas import MarketSchema



blp = Blueprint("Markets","markets",description="Operations on markets")



@blp.route("/markets/summaries")
class MarketsSummaries(MethodView):
    print("Market Summary class")
    ## Get Markets summaries 
    @jwt_required()
    @blp.response(200, MarketSchema(many=True))
    def get(self):
        
        try:
            response = requests.get("https://api.bittrex.com/v3/markets/summaries")
            return response.json()
        except requests.Timeout:
            abort(404, message="Page not found.")



@blp.route("/markets/<string:marketSymbol>/summary")
class MarketSymbol(MethodView):
    print("MarketSymbol class")
    ## Get Market summary based on marketSymbol
    @jwt_required()
    @blp.response(200, MarketSchema)
    def get(self, marketSymbol):
        try:
            response = requests.get(f"https://api.bittrex.com/v3/markets/{marketSymbol}/summary")
            return response.json()
        except requests.Timeout:
            abort(404, message="Market symbol not found.")