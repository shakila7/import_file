from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit='sale.order'

    status = fields.Selection([
            ('to_approve', 'To approve'),
            ('rejected','File rejected'),
            ('approved','File approved')], string='Status', default='to_approve')
    file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")
    reason = fields.Text(string='Reason')

    def approve_file(self):
        self.status = 'approved'
        return True

    def reject_file(self):
        self.status = 'rejected'
        self.file = ''
        return True

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        if (self.advance_payment_method == 'percentage' and self.amount <= 0.00) or (self.advance_payment_method == 'fixed' and self.fixed_amount <= 0.00):
            raise UserError(_('The value of the down payment amount must be positive.'))

        amount, name = self._get_advance_details(order)

        invoice_vals = self._prepare_invoice_values(order, name, amount, so_line)
        if order.status == 'approved' and order.file:
            invoice_vals['file'] = order.file
            invoice_vals['file_name'] = order.file_name
        if order.fiscal_position_id:
            invoice_vals['fiscal_position_id'] = order.fiscal_position_id.id
        invoice = self.env['account.move'].sudo().create(invoice_vals).with_user(self.env.uid)
        invoice.message_post_with_view('mail.message_origin_link',
                    values={'self': invoice, 'origin': order},
                    subtype_id=self.env.ref('mail.mt_note').id)
        return invoice
