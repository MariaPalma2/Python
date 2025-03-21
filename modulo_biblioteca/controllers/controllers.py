# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloBiblioteca(http.Controller):
#     @http.route('/modulo_biblioteca/modulo_biblioteca', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_biblioteca/modulo_biblioteca/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_biblioteca.listing', {
#             'root': '/modulo_biblioteca/modulo_biblioteca',
#             'objects': http.request.env['modulo_biblioteca.modulo_biblioteca'].search([]),
#         })

#     @http.route('/modulo_biblioteca/modulo_biblioteca/objects/<model("modulo_biblioteca.modulo_biblioteca"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_biblioteca.object', {
#             'object': obj
#         })

