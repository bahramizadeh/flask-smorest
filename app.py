import requests
from flask import Flask
from flask_smorest import abort, Blueprint, Api
from schemas import MarketSchema



app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "MARKET SYMMARY REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)


markets_summaries = Blueprint("markets", "__name__", description="Get Markets summaries")
market_symbol_summary = Blueprint("marketSymbol", "__name__", description="Get Market summary based on marketSymbol")


@markets_summaries.route("/markets/summaries")
@markets_summaries.response(200, MarketSchema(many=True))
def get_all_markets_summaries():
    
    try:
        response = requests.get("https://api.bittrex.com/v3/markets/summaries")
        return response.json()
    except requests.Timeout:
        abort(404, message="Page not found.")



@market_symbol_summary.route("/markets/<string:marketSymbol>/summary")
@market_symbol_summary.response(200, MarketSchema)
def get_market_sammary(marketSymbol):
    try:
        response = requests.get(f"https://api.bittrex.com/v3/markets/{marketSymbol}/summary")
        return response.json()
    except requests.Timeout:
        abort(404, message="Market symbol not found.")
        
        
        
        
api.register_blueprint(markets_summaries)
api.register_blueprint(market_symbol_summary)