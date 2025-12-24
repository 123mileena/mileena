from odoo import api, fields, models


class ShippingVessels(models.Model):
    _name = "ship.vessel"
    _description = "Fligh/Vessel/ Truck"

    code = fields.Char(string='Vessel Code', required=True)
    name = fields.Char(string='Vessel Name', required=True)
    short = fields.Char(string='Short Name')
    career_id = fields.Many2one('ship.carriers', string="Carrier", required=True)
    # carrier_type = fields.Selection('ship.carriers', related='carriers_id.type', string="Type")
    owner = fields.Char(string='Owner')
    country_id = fields.Many2one('res.country', string='Country')
    note = fields.Text(string='Note')
