from odoo import api, fields, models


class Employee(models.Model):
    _name = "employee"
    _description = "Employee"
    _order = "id desc"

    name = fields.Char(string='Name', required=True, tracking=True)
    phone_number = fields.Integer(string='Phone number', tracking=True)
    id_number = fields.Integer(string='Identify number', tracking=True)
    email = fields.Text(string='email')
    address = fields.Char(string='Name', required=True, tracking=True)
    bank_account = fields.Integer(string='Bank account')
    birthday = fields.Date(string="Birthday")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string="Patient Image")

