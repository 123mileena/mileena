from odoo import api, fields, models

class ShippingCommcategory (models.Model):
     _name = "ship.commcategory"
     _description = "Commodity Category"

     code = fields.Char(string = 'Category Code', required = True )
     name = fields.Char(string = 'Category Description', required = True)
