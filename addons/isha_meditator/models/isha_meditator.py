from odoo import fields, models

class IshaMeditator(models.Model):
    _name = 'isha.meditator'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="DoB")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")
    programs = fields.Many2many(comodel_name='isha.program', string="Programs")
    level = fields.Selection([('0', ''), ('basic', 'Basic'),('intermediate', 'Intermediate'), ('advanced', 'Advanced')], string='Level')
    interesed_in_it = fields.Boolean("Intereseted in IT?")