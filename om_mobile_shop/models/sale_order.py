from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
# employee -- many2one
    buy_type = fields.Selection([
        ('BuyNow', 'Buy Now'),
        ('InstallmentPurchase', 'Installment Purchase'),
    ], required=True, default='BuyNow', tracking=True)
