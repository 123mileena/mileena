from odoo import api, fields, models


class ShippingJobstatus(models.Model):
    _name = "ship.jobstatus"
    _description = "Shipment Job status"

    name = fields.Char(string='Job Status',required=True)
    code = fields.Char(stirng='Job Status Code',required=True,size=3)


