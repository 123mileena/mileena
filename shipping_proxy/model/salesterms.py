from odoo import api, fields, models

class ShippingSalesterms(models.Model):
     _name = "ship.salesterms"
     _description = "Sales Terms"
     _rec_name = "display_name"

     code = fields.Char(string = 'Terms Code', required=True)
     name = fields.Char(string = 'Terms Description', required=True)
     display_name = fields.Char(string='Display Name', compute='_compute_display_name')

     @api.depends('code', 'name')
     def _compute_display_name(self):
          for rec in self:
               rec.display_name = f"[{rec.code}] {rec.name}" if rec.code else rec.name