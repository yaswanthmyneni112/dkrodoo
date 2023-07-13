from odoo import fields, models, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import date
import logging
_logger = logging.getLogger(__name__)

class IshaMeditator(models.Model):
    _name = 'isha.meditator'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Char(string="Age", compute="_compute_age")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")
    programs = fields.Many2many(comodel_name='isha.program', string="Programs")
    level = fields.Selection([('0', ''), ('basic', 'Basic'),('intermediate', 'Intermediate'), ('advanced', 'Advanced')], string='Level')
    interested_in_it = fields.Boolean("Interested in IT?")
    phone_country_code = fields.Many2one(comodel_name="res.country")
    phone_number = fields.Char(string="Phone")

    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    country_id = fields.Many2one(comodel_name="res.country")
    currency_id = fields.Many2one(related="country_id.currency_id")
    state_id = fields.Many2one(comodel_name="res.country.state", domain="[('country_id', '=', country_id)]")
    zip_code = fields.Char(string="Zip Code")
    nationality_id = fields.Many2one(comodel_name="res.country")

    is_overseas = fields.Selection([('undefined', 'Undefined'), ('yes', 'Yes'), ('no', 'No')],
                                   compute="_compute_is_overseas", string="Is Overseas", default='undefined',
                                   store=True)
    

    volunteer_ids = fields.One2many("isha.volunteer", "meditator_id", string="Volunteering")

    @api.constrains('street')
    def _check_street_length(self):
        for record in self:
            if record.street and len(record.street) < 10:
                raise ValidationError("Street name should be minimum of 10 Characters.")
    @api.depends("country_id", "nationality_id")
    def _compute_is_overseas(self):
        for rec in self:
            india = self.env.ref('base.in').id
            if rec.country_id.id == india and rec.nationality_id.id == india:
                rec.is_overseas = 'yes'
            else:
                rec.is_overseas = 'no'

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            age = ''
            if rec.dob:
                d1 = rec.dob
                d2 = date.today()
                rd = relativedelta(d2, d1)
                age = str(rd.years) + ' years'
            rec.age = age

    def action_open_volunteer_wizard(self):
        _logger.info(f"action_open_volunteer_wizard {self}")
        view_id = self.env.ref('isha_meditator.volunteer_wizard_view').id
        return {
            'name': 'Volunteer Wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'volunteer.wizard',
            'views': [(view_id, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
    



