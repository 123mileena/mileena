from odoo import api, fields, models

class ShippingDepartment(models.Model):
    _name = "ship.transport"
    _description = "Transport Type"

    name = fields.Char(string='Transport',required=True)
    code = fields.Char(string='Code',required=True,size=4)]



