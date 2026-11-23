from odoo import fields, models


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char()
    author = fields.Char()
    isbn = fields.Char()
    publish_year = fields.Integer()
    copy_ids = fields.One2many('library.copy', 'book_id')
