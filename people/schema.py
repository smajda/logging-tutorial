from marshmallow import Schema, fields, validate


class Person(Schema):
    name = fields.String(
        validate=[validate.Length(min=3)],
        required=True,
    )
    birthdate = fields.Date()
