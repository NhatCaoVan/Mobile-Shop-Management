from odoo import api, fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    state = fields.Many2one('res.partner.category', string='State')
    manufacturing_date = fields.Date(string="Manufacturing month")
    original = fields.Many2one('res.country', 'Original',
                               states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                               change_default=True, index=True, tracking=1)
    warranty = fields.Date('Warranty Expiration',
                           states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                           change_default=True, index=True, tracking=1)
