from odoo import models, api, fields, _
from datetime import datetime, date
from odoo.exceptions import UserError

class SaleWork(models.Model):

    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        print("This is the Override Function")
        res = super(SaleWork, self).action_confirm()
        return res

    def open_order_action(self):
        print("Success to call menu to function")
        return {
            'name': _('Sales Server Action'),
            'domain': [],
            'view_type': 'form',
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    sale_order = fields.Char(string="Sale Order practise")
