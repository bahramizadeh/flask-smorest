from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from db import db

from resources.user import blp as UserBluprint
from resources.market import blp as MarketBluprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "MARKET SYMMARY REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["JWT_SECRET_KEY"] = "Maryam"
# app.config["JWT_SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


jwt = JWTManager(app) 

api = Api(app)

with app.app_context():
    db.create_all()

# markets_summaries = Blueprint("markets", "__name__", description="Get Markets summaries")
# market_symbol_summary = Blueprint("marketSymbol", "__name__", description="Get Market summary based on marketSymbol")

# ## Get Markets summaries 
# @markets_summaries.route("/markets/summaries")
# @markets_summaries.response(200, MarketSchema(many=True))
# @jwt_required()
# def get_all_markets_summaries():
    
#     try:
#         response = requests.get("https://api.bittrex.com/v3/markets/summaries")
#         return response.json()
#     except requests.Timeout:
#         abort(404, message="Page not found.")


# ## Get Market summary based on marketSymbol
# @market_symbol_summary.route("/markets/<string:marketSymbol>/summary")
# @market_symbol_summary.response(200, MarketSchema)
# @jwt_required()
# def get_market_sammary(marketSymbol):
#     try:
#         response = requests.get(f"https://api.bittrex.com/v3/markets/{marketSymbol}/summary")
#         return response.json()
#     except requests.Timeout:
#         abort(404, message="Market symbol not found.")
        
        


api.register_blueprint(UserBluprint)        
api.register_blueprint(MarketBluprint)
