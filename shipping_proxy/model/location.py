from odoo import api, fields, models

class ShippingLocation(models.Model):
     _name = "ship.location"
     _description = "Location"

     code = fields.Char(string = 'UNLC Code', required=True)
     name = fields.Char(string='Location Name', required=True)
     shortname = fields.Char(string='Short Name')
     port_id = fields.Many2one('ship.port', string="Port")
     country_id = fields.Many2one('res.country')
     addr = fields.Text(string='Remarks')