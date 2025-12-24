from odoo import api, fields, models


class ShippingDepartment(models.Model):
    _name = "ship.mode"
    _description = "Shipment Mode"

    name = fields.Char(string=' Shipment Mode',required=True)



