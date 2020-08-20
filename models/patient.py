from odoo import models, api, fields, _
from datetime import datetime, date

class HospitalPatient(models.Model):
    _name = "hospital.patient"

    @api.multi
    def name_get(self):
        # print('Success Name Get Function')
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.patient_id, rec.name)))
        return res


    name = fields.Char(string="Name")
    contact_no = fields.Char(string="Contact")
    date = fields.Date(string="Date")
    patient_id = fields.Char(string="Patient ID")