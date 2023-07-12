# -*- coding: utf-8 -*-


from odoo import fields, models


class IshaProgram(models.Model):
    _name = 'isha.program'
    _sql_constraints = [('name', 'unique (name)', 'You can not have two programs with the same name!')]

    name = fields.Char(string="Name",required=True)