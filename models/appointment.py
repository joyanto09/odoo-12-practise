from odoo import models, api, fields, _
from datetime import datetime, date

class PatientAppointment(models.Model):
    _name = "patient.appointment"
    _description = "Patient Appointment"


    @api.model
    def default_get(self, fields):
        res = super(PatientAppointment, self).default_get(fields)
        print("success.......")
        res["name"] = 1
        return res

    name = fields.Many2one('hospital.patient', string="Name")
    date = fields.Date(string="Date", default=datetime.now().strftime('%Y-%m-%d'))
    serial_no = fields.Char(string="Serial No")