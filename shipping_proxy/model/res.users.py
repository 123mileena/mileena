from odoo import api, fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one('res.company', string='Branch')
    department_id = fields.Many2one('ship.department', string='Department')
