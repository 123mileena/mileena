from odoo import api, fields, models

class ShippingUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one('res.company', string='Branch')
    ship_department_id = fields.Many2one('ship.department', string='Department')
