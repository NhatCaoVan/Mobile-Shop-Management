from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    manufacturing_date = fields.Date(string="manufacturing month")
    activate = fields.Boolean(index=True, default=False)
    service_tag = fields.Char(string='Service tag', required=True, tracking=True)
    # Nhà nhập khẩu many2one
    #Dai ly bao hanh many2one
    original = fields.Selection([
        ('vmm', 'Vietnamese'),
        ('tha', 'Thailand'),
        ('tw', 'Taiwan'),
        ('chins', 'Chinese'),
        ('ind', 'Indian'),
        ('us', "United States"),
    ], required=True, tracking=True)
    return_time = fields.Selection([
        ('7', '7 day'),
        ('14', '14 day'),
        ('30', '30 day'),
        ('45', '45 day'),
        ('60', '60 day'),
    ], required=True, default='30', tracking=True)
    warranty = fields.Selection([
        ('1', '1 month'),
        ('3', '3 month'),
        ('6', '6 month'),
        ('12', '12 month'),
        ('18', '18 month'),
        ('24', '24 month'),
        ('36', '36 month'),
    ], required=True, default='12', tracking=True)


