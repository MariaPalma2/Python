from odoo import models, fields, api, exceptions
from datetime import timedelta, date

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    user_id = fields.Many2one('library.user', string="User", required=True)
    book_id = fields.Many2one('library.book', string="Book", required=True)
    loan_date = fields.Date(string="Loan Date", default=fields.Date.today)
    return_date = fields.Date(string="Return Date")
    state = fields.Selection([
        ('pending', 'Pending'),
        ('returned', 'Returned'),
        ('late', 'Late')
    ], string="State", default='pending')

    @api.model
    def create(self, vals):
        """
        - Valida que el usuario no tenga más de 3 libros prestados activos.
        - Verifica que el libro tenga copias disponibles.
        - Asigna la fecha de devolución automática (7 días después).
        - Evita que el mismo libro sea prestado si ya está en préstamo.
        - Reduce el stock del libro prestado.
        """
        user = self.env['library.user'].browse(vals['user_id'])
        book = self.env['library.book'].browse(vals['book_id'])

        # Validar límite de préstamos por usuario
        active_loans = self.env['library.loan'].search_count([
            ('user_id', '=', user.id),
            ('state', '=', 'pending')
        ])
        if active_loans >= 3:
            raise exceptions.UserError("This user already has 3 active loans.")

        # Verificar si el libro tiene copias disponibles
        if book.copies_available <= 0:
            raise exceptions.UserError("No copies available for this book.")

        # Evitar préstamos duplicados (el mismo libro ya prestado)
        existing_loan = self.env['library.loan'].search([
            ('book_id', '=', book.id),
            ('state', '=', 'pending')
        ])
        if existing_loan:
            raise exceptions.UserError("This book is already on loan.")

        # Reducir el stock de libros disponibles
        book.copies_available -= 1

        # Asignar fecha de devolución por defecto (7 días después)
        vals['return_date'] = date.today() + timedelta(days=7)

        return super(LibraryLoan, self).create(vals)

    def action_return_book(self):
        """ 
        - Aumenta el stock del libro cuando se devuelve.
        - Cambia el estado a 'Returned'.
        - Controla si se devolvió tarde y cambia el estado a 'Late'.
        """
        for loan in self:
            if loan.state == 'returned':
                raise exceptions.UserError("This book is already returned.")

            # Verificar si la devolución es tardía
            if loan.return_date and loan.return_date < date.today():
                loan.state = 'late'
            else:
                loan.state = 'returned'

            # Aumentar el stock del libro devuelto
            loan.book_id.copies_available += 1
