from marshmallow import Schema, fields

class MarketSchema(Schema):

    symbol = fields.Str(required=True)
    high = fields.Float(required=True, precision=10)
    low = fields.Float(required=True)
    volume = fields.Float(required=True)
    quoteVolume = fields.Float(required=True)
    percentChange = fields.Float(required=True)
    updatedAt = fields.Str(required=True)