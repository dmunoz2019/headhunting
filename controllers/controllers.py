# -*- coding: utf-8 -*-
# from odoo import http


# class Headhunting(http.Controller):
#     @http.route('/headhunting/headhunting', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/headhunting/headhunting/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('headhunting.listing', {
#             'root': '/headhunting/headhunting',
#             'objects': http.request.env['headhunting.headhunting'].search([]),
#         })

#     @http.route('/headhunting/headhunting/objects/<model("headhunting.headhunting"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('headhunting.object', {
#             'object': obj
#         })

