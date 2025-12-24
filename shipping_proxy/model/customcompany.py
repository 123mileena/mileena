from odoo import models, fields, api

class ShippingCompany(models.Model):
    _inherit = "res.company"

    company_code = fields.Char(string='Company Code',size=3,required=True)
    branch_code = fields.Char(string='Branch Code',size=3)
    is_branch = fields.Boolean(string="Is Branch", default=False)
    hbl_logo = fields.Image(string='HBL Logo',
        max_width=1024,
        max_height=1024,
        help="Upload company logo used in HBL documents"
    )

    # display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)
    #
    # @api.depends('company_code', 'branch_code', 'name', 'parent_id')
    # def _compute_display_name(self):
    #     for rec in self:
    #         if rec.parent_id:  # It's a branch
    #             rec.display_name = f"[{rec.branch_code}] {rec.name}" if rec.branch_code else rec.name
    #         else:  # It's a main company
    #             rec.display_name = f"[{rec.company_code}] {rec.name}" if rec.company_code else rec.name
    #
    # @api.onchange('parent_id')
    # def _onchange_parent_id(self):
    #     self.is_branch = bool(self.parent_id)

