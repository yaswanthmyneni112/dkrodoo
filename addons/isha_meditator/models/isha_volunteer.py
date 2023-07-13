# -*- coding: utf-8 -*-


from odoo import fields, models
from . import constants


class IshaVolunteer(models.Model):
    _name = 'isha.volunteer'

    meditator_id = fields.Many2one(comodel_name="isha.meditator")
    volunteer_type = fields.Selection(list(constants.VOLUNTEER_TYPE.items()), string='Volunteer Type')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    visit_status = fields.Selection(list(constants.VOLUNTEER_VISIT_STATUS.items()), string='Volunteer Visit Status')