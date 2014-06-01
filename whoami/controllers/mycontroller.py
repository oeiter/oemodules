# -*- coding: utf-8 -*-

from openerp import http
from openerp.addons.web.controllers import main

class mycontroller(main.Home):
    @http.route('/', auth='none')
    def index(self):
        return "Hello, world!"
