from odoo import fields, models
from dateutil.relativedelta import relativedelta

class estate_property(models.Model):
    _name = "estate_property"
    _description = "Test Model"

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From', copy=False, default=(fields.date.today()+relativedelta(months=3)))
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', copy=False, readonly=True)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection([('north','North'), ('south','South'), ('east','East'),('west','West')])
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
                            default='new', required=True, copy=False)