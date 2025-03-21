from odoo import models, api

class ReportActiveLoans(models.AbstractModel):
    _name = 'report.modulo_biblioteca.report_active_loans'
    _description = 'Reporte de Préstamos Activos'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['library.loan'].search([('state', '=', 'pending')])  
        return {
            'doc_ids': docids,
            'doc_model': 'library.loan',
            'docs': docs,
        }
