from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class WizardVolunteer(models.TransientModel):
    _name = 'wizard.volunteer'

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    
    def action_create(self):
        
        self.env['isha.volunteer']