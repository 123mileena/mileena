from odoo import api, fields, models

class ShippingCharges(models.Model):
     _inherit = "product.template"

     code = fields.Char(string='Code', size=10, required=True)
     charge_type = fields.Char(string='Type')
     charge_margin = fields.Float(string='Margin')
     sales_group = fields.Char(string='Sales Group')
     expense_group = fields.Char(string='Expense Group')
     accural_account_id = fields.Char(string='Accural GL Account')
     cost_account_id = fields.Char(string='Cost GL Account')
     revenue_account_id = fields.Char(string='Revenue GL Account')
     wip_account_id = fields.Char(string='WIP GL Account')
     department_id = fields.Many2one('ship.department', string='Department')

     @api.model
     def default_get(self, fields):
          res = super(ShippingCharges, self).default_get(fields)
          if 'company_id' in fields:
               res['company_id'] = self.env.company.id
          return res