# -*- coding: utf-8 -*-


from odoo import fields, models, api
from . import constants
from odoo.exceptions import ValidationError
from datetime import datetime


class IshaVolunteer(models.Model):
    _name = 'isha.volunteer'

    vol_num = fields.Char("Volunteer Number", readonly=True)
    meditator_id = fields.Many2one(comodel_name="isha.meditator")
    volunteer_type = fields.Selection(list(constants.VOLUNTEER_TYPE.items()), string='Volunteer Type')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    visit_status = fields.Selection(list(constants.VOLUNTEER_VISIT_STATUS.items()), string='Volunteer Visit Status', default="yet_to_arrive")

    @api.model
    def create(self, vals):
        if vals.get('vol_num', 'New') == 'New':
            vals['vol_num'] = self.env['ir.sequence'].next_by_code('isha.volunteer.number') or 'Error: Sequence not found!'
        return super(IshaVolunteer, self).create(vals)
    
    @api.constrains("start_date", "end_date")
    def _check_visit_duration(self):
        for rec in self:
            if rec.end_date <= rec.start_date:
                raise ValidationError("End date can't be less than or equal to Start date")
            if rec.volunteer_type == 'stv' and (rec.end_date - rec.start_date).days >= 30:
                raise ValidationError("Short term volunteering: Maximum 30 days")
            if rec.volunteer_type == 'ltv' and (rec.end_date - rec.start_date).days < 30:
                raise ValidationError("Long term volunteering minimum 30 days")
