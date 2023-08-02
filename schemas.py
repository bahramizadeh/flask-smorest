"""
    Using Marshmallow library to serialize and deserialize data  
    """
from marshmallow import Schema, fields

class MarketSchema(Schema):
    """
    this is a schema for serializing and deserializing the payload of Markect 
    """
    symbol = fields.Str(required=True)
    high = fields.Float(required=True, precision=7)
    low = fields.Float(required=True, precision=7)
    volume = fields.Float(required=True, precision=7)
    quoteVolume = fields.Float(required=True, precision=7)
    percentChange = fields.Float(required=True, precision=7)
    updatedAt = fields.Str(required=True)

class UserSchema(Schema):
    """
    this is a schema for serializing and deserializing the payload of User requests
    arguments: username and password
    """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    