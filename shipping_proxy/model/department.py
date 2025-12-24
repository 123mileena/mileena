from odoo import api, fields, models


class ShippingDepartment(models.Model):
    _name = "ship.department"
    _description = "Department"

    code = fields.Char(string='Code',required=True,size=3)
    name = fields.Char(string=' Department',required=True)
    transport_id = fields.Many2one('ship.transport', string='Transport', required=True,store=True)
    mode_id = fields.Many2one('ship.mode', string='Type', required=True)
    job_charges = fields.Boolean(string='Job Charges Applicable :')
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)

    @api.depends('code', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"[{rec.code}] {rec.name}" if rec.code else rec.name