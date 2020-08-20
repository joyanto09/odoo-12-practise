from odoo import models, api, fields, _
from datetime import datetime, date

class PatientAppointment(models.Model):
    _name = "patient.appointment"

    name = fields.Many2one('hospital.patient', string="Name")
    date = fields.Date(string="Date", default=datetime.now().strftime('%Y-%m-%d'))
    serial_no = fields.Char(string="Serial No")