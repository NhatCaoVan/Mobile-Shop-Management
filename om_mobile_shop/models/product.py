from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _order = "id desc"

    name = fields.Char(string='Name', required=True, tracking=True)
    # reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
    #                         default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    # state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
    #                           ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
    #                          string="Status", tracking=True)
    # responsible_id = fields.Many2one('res.partner', string="Responsible")
    image = fields.Binary(string="Patient Image")
    # appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")
