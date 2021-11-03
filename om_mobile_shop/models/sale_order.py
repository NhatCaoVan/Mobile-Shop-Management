from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    # fields Bao hiem roi vo
    # employee -- many2one
    buy_type = fields.Selection([
        ('BuyNow', 'Buy Now'),
        ('InstallmentPurchase', 'Installment Purchase'),
    ], required=True, default='BuyNow', tracking=True)
    employee_id = fields.Many2one(
        'hr.employee', string='Employees', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1)
