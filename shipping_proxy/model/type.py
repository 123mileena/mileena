from odoo import api, fields, models


class ShippingMode(models.Model):
    _name = "ship.type"
    _description = "Shipment Mode"

    name = fields.Char(string='Name',required=True)
    code = fields.Char(string='Code',required=True,size=4)

