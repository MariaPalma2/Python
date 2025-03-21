from odoo import models, api

class ReportRegisteredUsers(models.AbstractModel):
    _name = 'report.modulo_biblioteca.report_registered_users'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['library.user'].search([])
        return {
            'doc_ids': docids,
            'doc_model': 'library.user',
            'docs': docs,
        }