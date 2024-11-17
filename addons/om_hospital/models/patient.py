from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread'
    _description = 'Patient Records'

    name = fields.Char(string = 'Name' ,required =True)
    age = fields.Integer(string= 'Age')
    gender = fields.Selection([('male', 'Male'), ('female' , 'Female')],string='Gender')
    is_child = fields.Boolean(string= 'Is Child ?')
    notes = fields.Text(string='Notes')