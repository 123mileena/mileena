from odoo import api, fields, models

class ShippingServicelevel(models.Model):
    _name = "ship.servicelevel"
    _description = "Service Level"

    name = fields.Char(string='Service Level',required=True)
    code = fields.Char(string='Code',required=True,size=4)