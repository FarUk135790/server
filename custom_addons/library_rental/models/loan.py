from odoo import fields, models


class Loan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    copy_id = fields.Many2one(
        'library.copy',
        required=True,
        ondelete='restrict',
    )
    member_id = fields.Many2one(
        'library.member',
        required=True,
        ondelete='restrict',
    )
    loan_date = fields.Date(default=fields.Date.today)
    due_date = fields.Date()
    return_date = fields.Date()
    state = fields.Selection(
        [
            ('active', 'Активна'),
            ('returned', 'Повернена'),
        ],
        default='active',
        required=True,
    )

    copy_inventory_number = fields.Char(
        related='copy_id.inventory_number',
        readonly=True,
    )
    copy_condition = fields.Selection(
        related='copy_id.condition',
        readonly=True,
    )
    book_id = fields.Many2one(
        related='copy_id.book_id',
        readonly=True,
    )
    book_author = fields.Char(
        related='copy_id.book_id.author',
        readonly=True,
    )
    book_isbn = fields.Char(
        related='copy_id.book_id.isbn',
        readonly=True,
    )
    book_publish_year = fields.Integer(
        related='copy_id.book_id.publish_year',
        readonly=True,
    )
    member_name = fields.Char(
        related='member_id.name',
        readonly=True,
    )
    membership_number = fields.Char(
        related='member_id.membership_number',
        readonly=True,
    )
