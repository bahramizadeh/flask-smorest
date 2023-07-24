import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt

from schemas import MarketSchema



blp = Blueprint("Markets","markets",description="Operations on markets")



@blp.route("/markets/summaries")
class MarketsSummaries(MethodView):
    
    ## Get Markets summaries 
    @jwt_required()
    @blp.response(200, MarketSchema(many=True))
    def get(self):
        return self._get()


    def _get(self):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilage required.")
            
        try:
            response = requests.get("https://api.bittrex.com/v3/markets/summaries")
            return response.json()
        except Exception as err:
            abort(None, message=err)
            

            
@blp.route("/markets/<string:marketSymbol>/summary")
class MarketSymbol(MethodView):
    
    ## Get Market summary based on marketSymbol
    @jwt_required()
    @blp.response(200, MarketSchema)
    def get(self, marketSymbol):
        return self._get(marketSymbol)
            
            
            
    def _get(self, marketSymbol):
        try:
            response = requests.get(f"https://api.bittrex.com/v3/markets/{marketSymbol}/summary")
            return response.json()
        except Exception as err:
            abort(None, message=err)
            