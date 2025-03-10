from odoo import models, fields, api
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _get_sequence_number(self, move_type, journal_id):
        company_name = self.env.company.name
        current_year = datetime.now().year % 100
        current_month = datetime.now().month

        if move_type == 'in_invoice':
            prefix = 'BILLS'
            sequence = self.env['ir.sequence'].next_by_code('vendor.bill.sequence')
        elif move_type == 'out_invoice':
            prefix = 'INV'
            sequence = self.env['ir.sequence'].next_by_code('customer.invoice.sequence')
        elif move_type == 'entry':
            journal_code = journal_id.code if journal_id else 'UNKNOWN'
            sequence = self.env['ir.sequence'].next_by_code('journal.entry.sequence')
            prefix = journal_code
        else:
            return False

        return f'{prefix}/{company_name}/{current_year:02}/{current_month:02}/{sequence}'

    @api.model
    def create(self, vals):
        move_type = vals.get('move_type')
        journal_id = self.env['account.journal'].browse(vals.get('journal_id'))

        if move_type in ['in_invoice', 'out_invoice', 'entry']:
            vals['name'] = self._get_sequence_number(move_type, journal_id)
        return super(AccountMove, self).create(vals)
