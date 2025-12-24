from odoo import api, fields, models, _


class ShippingForwardagent(models.Model):
    _inherit = "res.partner"

    # forward_code = fields.Char(string="Code", required=True, copy=False, readonly=False, default=lambda self: _('New'))

    forward_agent = fields.Boolean(string='Forward Agent')
    forward_code = fields.Char(string='Agent Reference')
    customer_code = fields.Char(string='Customer Reference')
    vendor_code = fields.Char(string='VendorReference')

    # @api.model
    # def create(self, vals):
    #       if vals.get('code', _('New')) == _('New'):
    #             vals['code'] = self.env['ir.sequence'].next_by_code('res.partner') or _('New')
    #       return super(ShippingForwardagent, self).create(vals)

    @api.model
    def create(self, vals):
          record = super(ShippingForwardagent, self).create(vals)

          if vals.get('customer_rank', 0) > 0:
                sequence = self.env['ir.sequence'].next_by_code('res.partner.customer')
                record.customer_code = sequence
          elif vals.get('supplier_rank', 0) > 0:
                sequence = self.env['ir.sequence'].next_by_code('res.partner.vendor')
                record.vendor_code = sequence
          elif vals.get('forward_agent', True):
                sequence = self.env['ir.sequence'].next_by_code('res.partner.forwarding_agent')
                record.forward_code = sequence
          return record

