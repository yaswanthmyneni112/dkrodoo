from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class VolunteerWizard(models.TransientModel):
    _name = 'volunteer.wizard'

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    
    def action_create(self):
        model = self.env.context.get('active_model')
        record_id = self.env.context.get('active_id')
        _logger.info(f"LOG: {model}, {record_id}")
        self.env['isha.volunteer'].create({
            'meditator_id': record_id,
            # 'volunteer_type': ,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'visit_status': 'yet_to_arrive',
        })
