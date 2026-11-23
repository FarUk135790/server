from odoo import fields, models


class Member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(required=True)
    membership_number = fields.Char(required=True)

    _membership_number_unique = models.Constraint(
        'unique(membership_number)',
        'Membership numbers must be unique.',
    )
