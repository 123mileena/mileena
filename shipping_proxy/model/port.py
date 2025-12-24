from odoo import api, fields, models


class ShippingPort(models.Model):
    _name = "ship.port"
    _description = "Port Master"
    _rec_name = "display_name"

    code = fields.Char(string='Port Code', required=True)
    name = fields.Char(string='Port Name', required=True)
    short = fields.Char(string='Short Name')
    country_id = fields.Many2one('res.country', string='Country')
    subdivsion = fields.Char(string='Sub Division')
    airmode = fields.Boolean(string='Air')
    seamode = fields.Boolean(string='Sea')
    landmode = fields.Boolean(string='Land')
    remarks = fields.Text(string='Remarks')
    display_name = fields.Char(string='Display Name', compute='_compute_display_name',store=True)

    @api.depends('code', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.code}] {rec.name}" if rec.code else rec.name