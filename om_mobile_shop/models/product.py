from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    model_id = fields.Many2one('fleet.vehicle.model', 'Model',
                               tracking=True, required=True, help='Model of the vehicle')
