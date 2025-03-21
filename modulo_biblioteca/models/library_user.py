from odoo import models, fields

class LibraryUser(models.Model):
    _name = 'library.user'
    _description = 'Library User'

    name = fields.Char(string="Full Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    registration_date = fields.Date(string="Registration Date", default=fields.Date.today)
