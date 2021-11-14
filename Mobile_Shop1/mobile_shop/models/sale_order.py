# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    buy_type = fields.Selection([
        ('BuyNow', 'Buy Now'),
        ('InstallmentPurchase', 'Installment Purchase'),
    ], required=True, default='BuyNow', tracking=True)

    employee_id = fields.Many2one(
        'hr.employee', string='Employees', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1)
    # compute discount
    discount_total = fields.Monetary(
        compute="_compute_discount_total",
        string="Discount Subtotal",
        currency_field="currency_id",
        store=True,
    )
    price_total_no_discount = fields.Monetary(
        compute="_compute_discount_total",
        string="Subtotal Without Discount",
        currency_field="currency_id",
        store=True,
    )

    @api.depends("order_line.discount_total", "order_line.price_total_no_discount")
    def _compute_discount_total(self):
        for order in self:
            discount_total = sum(order.order_line.mapped("discount_total"))
        price_total_no_discount = sum(
            order.order_line.mapped("price_total_no_discount")
        )
        order.update(
            {
                "discount_total": discount_total,
                "price_total_no_discount": price_total_no_discount,
            }
        )
    # compute shipping
    shipping_amount_total = fields.Float(
        compute="_compute_shipping", digits="Account", store=True
    )
    shipping_amount_untaxed = fields.Float(
        compute="_compute_shipping", digits="Account", store=True
    )
    shipping_amount_tax = fields.Float(
        compute="_compute_shipping", digits="Account", store=True
    )
    item_amount_total = fields.Float(
        compute="_compute_shipping", digits="Account", store=True
    )
    item_amount_untaxed = fields.Float(
        compute="_compute_shipping", digits="Account", store=True
    )
    item_amount_tax = fields.Float(
        compute="_compute_shipping", digits="Account", store=True
    )

    @api.depends("amount_total", "amount_untaxed")
    def _compute_shipping(self):
        for record in self:
            shipping_amount_untaxed = shipping_amount_total = shipping_amount_tax = 0
            for line in record.order_line:
                if not line.is_delivery:
                    continue
                shipping_amount_untaxed += line.price_subtotal
                shipping_amount_total += line.price_total
                shipping_amount_tax += line.price_tax
            record.update(
                {
                    "shipping_amount_untaxed": shipping_amount_untaxed,
                    "shipping_amount_total": shipping_amount_total,
                    "shipping_amount_tax": shipping_amount_tax,
                }
            )
            for key in ["amount_total", "amount_untaxed", "amount_tax"]:
                record["item_%s" % key] = record[key] - record["shipping_%s" % key]
