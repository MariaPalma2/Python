from odoo import models, api

class ReportLoanHistory(models.AbstractModel):
    _name = 'report.modulo_biblioteca.report_loan_history'
    _description = 'Reporte Histórico de Préstamos'

    @api.model
    def _get_report_values(self, docids=None, data=None):
        # Buscar todos los préstamos sin filtro (se puede modificar para buscar solo devueltos o en cierto periodo)
        docs = self.env['library.loan'].search([])  
        
        return {
            'doc_ids': docids if docids else docs.ids,  # Asegurar que doc_ids siempre tenga valores
            'doc_model': 'library.loan',
            'docs': docs,
        }
