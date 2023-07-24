import pytest
from unittest.mock import Mock, patch
from resources.user import UserRegister, User
from models.user import UserModel

@patch("resources.user.db")
@patch("resources.user.UserModel")
def test_user_register(mock_um, db):
    user_info = {
        "username": "admin",
        "password": "testpassword"
    }
    mock_um.query.filter(UserModel.username==user_info["username"]).first.return_value = None
    user_register = UserRegister()
    user_register._post(user_info)


@patch("resources.user.db")
@patch("resources.user.UserModel")
def test_user_register_abort(mock_um, db):
    user_info = {
        "username": "admin",
        "password": "testpassword"
    }
    
    
    user = UserModel(**user_info)
    mock_um.query.filter(UserModel.username==user_info["username"]).first.return_value = user
    user_register = UserRegister()
    with pytest.raises(Exception):
        user_register._post(user_info)


