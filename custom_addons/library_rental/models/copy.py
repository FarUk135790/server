from odoo import fields, models


class Copy(models.Model):
    _name = 'library.copy'
    _description = 'Book Copy'

    book_id = fields.Many2one(
        'library.book',
        required=True,
        ondelete='restrict',
    )
    inventory_number = fields.Char()
    condition = fields.Selection(
        [
            ('new', 'Новий'),
            ('good', 'Добрий'),
            ('damaged', 'Пошкоджений'),
        ]
    )
