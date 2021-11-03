from odoo import api, fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    manufacturing_date = fields.Date(string="manufacturing month")
    original = fields.Many2one('res.country', 'Country',
                               states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                               required=True, change_default=True, index=True, tracking=1)
    warranty = fields.Date('Warranty Expiration',
                           states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                           required=True, change_default=True, index=True, tracking=1)
