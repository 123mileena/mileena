from odoo import api, fields, models

class ShippingCommodity(models.Model):
    _name = "ship.commodity"
    _description = "Commodity Master"

    name = fields.Char(string='Commodity Name', required=True)
    code = fields.Char(string='Commodity Code', required=True)
    categ_id = fields.Many2one('ship.commcategory', string="Category", required=True)
    hscode = fields.Char(string='HS Code')
    short = fields.Char(string='Short Name')
    uom_id = fields.Many2one('uom.uom', string='UOM')
    country_id = fields.Many2one('res.country', string="Country")
    note = fields.Text(string='Remarks')
