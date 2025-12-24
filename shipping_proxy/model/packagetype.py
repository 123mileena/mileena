from odoo import api, fields, models

class ShippingPackagetype (models.Model):
     _name = "ship.packagetype"
     _description = "Package Type Master"

     code = fields.Char(string = 'Code', required = True )
     name = fields.Char(string = 'Name', required = True)
     short = fields.Char(string = 'Short Name')
     note = fields.Text (string = "Note")