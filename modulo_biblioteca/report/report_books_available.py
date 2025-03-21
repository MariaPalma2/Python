from odoo import models, api

class ReportBooksAvailable(models.AbstractModel):
    _name = 'report.modulo_biblioteca.report_books_available'
    _description = 'Reporte de Libros Disponibles'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['library.book'].search([('copies_available', '>', 0)])  # Libros con copias disponibles
        return {
            'doc_ids': docids,
            'doc_model': 'library.book',
            'docs': docs,
        }
