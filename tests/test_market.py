import requests
import pytest
from unittest.mock import Mock, patch, MagicMock
from resources.market import MarketsSummaries, MarketSymbol, blp
from app import app

        
def mocked_result():
    mocked_response = Mock()
    mocked_response.json.return_value = {
        "high": 0.00328917,
        "low": 0.00312004,
        "percentChange": 0.12,
        "quoteVolume": 1.10779107,
        "symbol": "LTC-BTC",
        "updatedAt": "2023-07-22T16:55:19.987Z",
        "volume": 352.28109405
    }
    return mocked_response 


@patch("resources.market.requests")
def test_market_symbol(mock_req):
    
    market_symbol = MarketSymbol()
    symbol = "LTC-BTC"
    mock_req.get.return_value = mocked_result()
    response = market_symbol._get(symbol)

    assert response == {'high': 0.00328917, 'low': 0.00312004, 'percentChange': 0.12, 'quoteVolume': 1.10779107, 'symbol': 'LTC-BTC', 'updatedAt': '2023-07-22T16:55:19.987Z', 'volume': 352.28109405}
    mock_req.get.assert_called()


@patch("resources.market.requests")
def test_market_symbol_exception(mock_req):
    market_symbol = MarketSymbol()
    symbol = "LTC-BTC"
    mock_req.get.side_effect = Exception
    with pytest.raises(Exception):
        response = market_symbol._get(symbol)
    
    
    
def mocked_result_for_markets_summaries():
    mocked_response = Mock()
    mocked_response.json.return_value = [
                                            {
                                                "high": 7.45e-06,
                                                "low": 7.45e-06,
                                                "percentChange": 0.0,
                                                "quoteVolume": 0.0,
                                                "symbol": "1ECO-BTC",
                                                "updatedAt": "2023-07-23T14:21:01.447Z",
                                                "volume": 0.0
                                            },
                                            {
                                                "high": 0.28531,
                                                "low": 0.28194,
                                                "percentChange": -0.53,
                                                "quoteVolume": 142.72875704,
                                                "symbol": "1ECO-USDT",
                                                "updatedAt": "2023-07-23T14:55:02.203Z",
                                                "volume": 503.513
                                            }
                                        ]
    return mocked_response

    

@patch("resources.market.get_jwt")
@patch("resources.market.requests")
def test_markets_summaries(mock_req, mock_get_jwt):
    
    mock_get_jwt.return_value = {"is_admin": True}
    markets_summeries = MarketsSummaries()
    mock_req.get.return_value = mocked_result_for_markets_summaries()
    response = markets_summeries._get()

    assert response == [
        {
            "high": 7.45e-06,
            "low": 7.45e-06,
            "percentChange": 0.0,
            "quoteVolume": 0.0,
            "symbol": "1ECO-BTC",
            "updatedAt": "2023-07-23T14:21:01.447Z",
            "volume": 0.0
        },
        {
            "high": 0.28531,
            "low": 0.28194,
            "percentChange": -0.53,
            "quoteVolume": 142.72875704,
            "symbol": "1ECO-USDT",
            "updatedAt": "2023-07-23T14:55:02.203Z",
            "volume": 503.513
        }
    ]


@patch("resources.market.get_jwt")
@patch("resources.market.requests")
def test_markets_summaries_not_admin(mock_req, mock_get_jwt):
    
    mock_get_jwt.return_value = {"is_admin": False}
    markets_summeries = MarketsSummaries()
    mock_req.get.side_effect = Exception
    with pytest.raises(Exception):
        response = markets_summeries._get()

    
@patch("resources.market.get_jwt")
@patch("resources.market.requests")
def test_markets_summaries_exception(mock_req, mock_get_jwt):
    
    markets_summeries = MarketsSummaries()
    mock_get_jwt.return_value = {"is_admin": True}
    mock_req.get.side_effect = Exception
    with pytest.raises(Exception):
        response = markets_summeries._get()