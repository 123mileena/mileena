from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ShippingUnlocode(models.Model):
    _name = "ship.unlocode"
    _description = "Transport Location"

    name = fields.Char(string='Name', required=True)
    unlocode_code = fields.Char(string='ULOCODE', required=True, size=5)
    unlocode_port_id = fields.Many2one('ship.port', string='Port')
    unlocode_country_id = fields.Many2one('res.country', string="Country")
    # display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)
    _sql_constraints = [
        ('unlocode_code_unique', 'unique(unlocode_code)', 'UNLOCODE must be unique.'),
    ]

    # @api.depends('unlocode_code', 'name')
    # def _compute_display_name(self):
    #     for rec in self:
    #         rec.display_name = f"[{rec.unlocode_code}] {rec.name}" if rec.unlocode_code else rec.name

    @api.onchange('unlocode_code')
    def _onchange_unlocode_code(self):
        for rec in self:
            if rec.unlocode_code:
                code = rec.unlocode_code.strip().upper()
                rec.unlocode_code = code  # update the field with cleaned version

                # Only check uniqueness if it's a saved record (has ID)
                domain = [('unlocode_code', '=', code)]
                if rec.id:
                    domain.append(('id', '!=', rec.id))

                existing = self.env['ship.unlocode'].search(domain, limit=1)
                if existing:
                    raise ValidationError(f"UNLOCODE '{code}' already exists.")

    # @api.constrains('unlocode_code')
    # def _check_unlocode_code_valid(self):
    #     for rec in self:
    #         code = (rec.unlocode_code or "").strip().upper()
    #         if len(code) != 5:
    #             raise ValidationError("UNLOCODE must be exactly 5 characters.")
    #         rec.unlocode_code = code

    @api.model
    def create(self, vals):
        if 'unlocode_code' in vals:
            vals['unlocode_code'] = vals['unlocode_code'].strip().upper()
        return super().create(vals)
