from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    author_id = fields.Many2one('library.author', string="Author")
    category_id = fields.Many2one('library.category', string="Category")
    copies_available = fields.Integer(string="Copies Available", default=1)
