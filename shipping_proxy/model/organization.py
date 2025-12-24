from odoo import api, fields, models, _

class ShippingOrganization(models.Model):
    _inherit = "res.partner"

    code = fields.Char(string='Code',size=12)
    active_client = fields.Boolean(string='Active Client',default=True)
    national_account = fields.Boolean(string='National Account')
    global_supplier = fields.Boolean(string='Global Supplier')
    temp_account = fields.Boolean(string='Temporary Account')
    receivable_acct = fields.Boolean(string='Receivables')
    payable_acct = fields.Boolean(string='Payables')
    consigner = fields.Boolean(string='Consignor')
    consignee = fields.Boolean(string='Consignee')
    transprt_client = fields.Boolean(string='Transport Client')
    warehouse = fields.Boolean(string='Warehouse')
    carrier = fields.Boolean(string='Carrier')
    forward_agent = fields.Boolean(string='Forward Agent')
    broker = fields.Boolean(string='Broker')
    services = fields.Boolean(string='Services')
    competitor = fields.Boolean(string='Competitor')
    sales = fields.Boolean(string='Sales')
    control_agent = fields.Boolean(string='Controling Agent')
    unlocode_id = fields.Many2one('ship.unlocode', string='UNLOC',store=True)
    code_warning = fields.Char(string="Code Warning", readonly=True)
    company_code = fields.Char(string='code', size=3)
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company
    )

    @api.model
    def create(self, vals):
        # Check and set customer/vendor based on receivable and payable fields when creating
        if vals.get('receivable_acct'):
            vals['customer_rank'] = 1  # Marks as customer
        if vals.get('payable_acct'):
            vals['supplier_rank'] = 1  # Marks as vendor
        return super(ShippingOrganization, self).create(vals)

    def write(self, vals):
        # Update customer/vendor status based on receivable and payable fields
        if 'receivable_acct' in vals:
            vals['customer_rank'] = 1 if vals['receivable_acct'] else 0
        if 'payable_acct' in vals:
            vals['supplier_rank'] = 1 if vals['payable_acct'] else 0
        return super(ShippingOrganization, self).write(vals)

    @api.onchange('name', 'unlocode_id', 'company_id')
    def _generate_custom_code(self):
        for record in self:
            if record.name and record.unlocode_id:
                unlocode = record.unlocode_id.unlocode_code or ""
                company_code = record.company_id.company_code or ""
                name_parts = record.name.split()

                part1 = name_parts[0][:3].upper() if len(name_parts) > 0 else ""
                part2 = name_parts[1][:3].upper() if len(name_parts) > 1 else ""
                part3 = unlocode[-3:].upper() if len(unlocode) >= 5 else unlocode.upper()

                generated_code = f"{part1}{part2}{part3}"
                # generated_code = f"{company_code}{part1}{part2}{part3}"

                # Search for similar codes in the same company
                similar_codes = self.env['res.partner'].search([
                    ('code', '=like', f"{generated_code}%"),
                    ('company_id', '=', record.company_id.id)
                ])

                suffix_numbers = []
                for code in similar_codes:
                    suffix = code.code.replace(generated_code, "")
                    if suffix.isdigit():
                        suffix_numbers.append(int(suffix))

                next_suffix = max(suffix_numbers, default=0) + 1

                record.code = f"{generated_code}{next_suffix}" if similar_codes else generated_code

                # Optional: set warning if duplicate exists
                record.code_warning = (
                    f"Duplicate code detected: {generated_code}. Next available code: {record.code}"
                    if similar_codes else ""
                )
            else:
                record.code = ""
                record.code_warning = ""

    def action_open_partner_search(self):
        return {
            'name': 'Search Partner',
            'type': 'ir.actions.act_window',
            'res_model': 'partner.search.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id}
        }



