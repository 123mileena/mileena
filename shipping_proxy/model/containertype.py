from odoo import api, fields, models

class ShippingContianertype (models.Model):
     _name = "ship.containertype"
     _description = "Container Type Master"
     _rec_name = "display_name"

     code = fields.Char(string = 'TypeCode', required = True )
     name = fields.Char(string = 'Type Name', required = True)
     short = fields.Char(string = 'Short Name')
     container_type = fields.Char(string='Container')
     transport_id = fields.Many2one('ship.transport', string='Transport')
     length = fields.Float(string = "Length")
     length_id = fields.Selection([
        ('cent', 'Centimeter'),
        ('mtr', 'Meter'), ], string='Length Uom')
     width = fields.Float(string = "Width")
     width_id = fields.Selection([
          ('cent', 'Centimeter'),
          ('mtr', 'Meter'), ], string='Width Uom')
     height = fields.Float(string = "Height")
     height_id = fields.Selection([
          ('cent', 'Centimeter'),
          ('mtr', 'Meter'), ], string='Height Uom')
     volume = fields.Float(string = "Volume")
     volume_id = fields.Selection([
          ('cum', 'Cubic meter'),
          ('ltr', 'Litre'), ], string='Volume Uom')
     weight = fields.Float(string = "Weight")
     weight_id = fields.Selection([
          ('kg', 'Kilogram'), ], string='Weight Uom')
     tare_weight = fields.Float(string="Tare Weight")
     gross_weight = fields.Float(string="Gross Weight")
     volweight = fields.Float(string = "Volume Weight")
     volweight_id = fields.Selection([
          ('kg', 'Kilogram'), ], string='Vol Weight Uom')
     note = fields.Text (string = "Note")

     display_name = fields.Char(string='Display Name', compute='_compute_display_name',store=True)

     @api.depends('code', 'name')
     def _compute_display_name(self):
          for rec in self:
               rec.display_name = f"[{rec.code}] {rec.name}" if rec.code else rec.name