from odoo import models, fields, api


class ShippingDashboard(models.Model):
    _name = "ship.dashboard"
    _description = "Shipping Dashboard"
    # _auto = False  # No database table is created

    name = fields.Char(default="Dashboard")  # Required for Kanban view
    date = fields.Date(string="Date", default=fields.Date.today)
    total_quotations = fields.Integer(string=" Total Quotations", readonly=True)
    total_bookings = fields.Integer(string=" Total Bookings", readonly=True)
    active_shipments = fields.Integer(string=" Active Shipments", readonly=True)
    pending_job_orders = fields.Integer(string=" Pending Job Orders", readonly=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('invoice', 'Invoiced'),
        ('cancel', 'Cancelled')],
        string='Status'
    )

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        """Override search_read to return computed values dynamically in Odoo 17."""
        if fields is None:
            fields = ["name", "date", "total_quotations", "total_bookings", "active_shipments", "pending_job_orders"]

        # Compute real-time statistics
        total_quotations = self.env["ship.quote"].search_count([("state", "=", "confirm")])
        total_bookings = self.env["ship.booking"].search_count([])
        active_shipments = self.env["ship.shipment"].search_count([("state", "=", "confirm")])
        pending_job_orders = self.env["ship.joborder"].search_count([("state", "=", "draft")])

        # Return computed record
        return [{
            "id": 1,  # Required for Odoo views
            "name": "Dashboard",
            # "date": fields.Date.context_today(self.env['ship.dashboard']),
            "total_quotations": total_quotations,
            "total_bookings": total_bookings,
            "active_shipments": active_shipments,
            "pending_job_orders": pending_job_orders,
        }]

    def read(self, fields=None, load='_classic_read'):
        """Override read to prevent SQL query errors."""
        return self.search_read(fields=fields, limit=1)
