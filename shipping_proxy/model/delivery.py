from odoo import api, fields, models


class ShippingDelivery(models.Model):
    _name = "ship.delivery"
    _description = "Delivery Mode"

    name = fields.Char(string='Name', required=True)
