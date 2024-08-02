from odoo import fields, models

class estate_property_type(models.Model):
    _name = "estate_property_type"
    _description = "Estate property type"

    name = fields.Char(required=True)