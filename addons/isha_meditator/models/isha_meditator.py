# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class IME_Product_Product(models.Model):
    _name = 'ime.product.product'
    _sql_constraints = [('name', 'unique (name)', 'You can not have two product with the same name!')]
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = "IME Product Product"
    _order = "name"

    def _get_default_uom_id(self):
        return self.env["uom.uom"].search([], limit=1, order='id').id

    name = fields.Char(string="Name",required=True)
    active = fields.Boolean(string="Active",default=True)
    remarks = fields.Text('Product Remarks', translate=True)
    uom_id = fields.Many2one('uom.uom', 'Unit of Measure',default=_get_default_uom_id, required=True,
        help="Default unit of measure used for all stock operations.")
    tax_id = fields.Many2one('account.tax', string='Taxes')
    unit_price = fields.Float('Unit Price', default=1.0,digits='Product Price',help="Unit price of the product.")
    type = fields.Selection([('purchase', 'Purchase'),('service', 'Service')], string='Product Type', default='purchase', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')