from odoo import api, fields, models

class ShippingCarriers(models.Model):
     _name = "ship.carriers"
     _description = "Carriers"

     code = fields.Char(string = 'Carrier Code', required = True )
     name = fields.Char(string = 'Carrier Name', required = True)
     short = fields.Char(string = 'Short Name')
     carrier_type_id = fields.Many2one('ship.mode',string='Carrier type')


