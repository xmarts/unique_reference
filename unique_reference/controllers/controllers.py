# -*- coding: utf-8 -*-
from odoo import http

# class UniqueReference(http.Controller):
#     @http.route('/unique_reference/unique_reference/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unique_reference/unique_reference/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unique_reference.listing', {
#             'root': '/unique_reference/unique_reference',
#             'objects': http.request.env['unique_reference.unique_reference'].search([]),
#         })

#     @http.route('/unique_reference/unique_reference/objects/<model("unique_reference.unique_reference"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unique_reference.object', {
#             'object': obj
#         })