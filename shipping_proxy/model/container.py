from odoo import api, fields, models

class ShippingContianertype (models.Model):
     _name = "ship.container"
     _description = "Container Master"
     _rec_name = "display_name"

     code = fields.Char(string = 'Code', required = True,size=3 )
     name = fields.Char(string = 'Name', required = True)
     display_name = fields.Char(string='Display Name', compute='_compute_display_name')

     @api.depends('code', 'name')
     def _compute_display_name(self):
          for rec in self:
               rec.display_name = f"[{rec.code}] {rec.name}" if rec.code else rec.name