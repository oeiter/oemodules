# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "simpleblog",
    # short description, used as subtitles on modules listings
    'summary': "this is a simple blog system to writing blog",
    # long description of module purpose
    'description': """
    in nowdays life, you may want to write down the content of your life and work, just writing
""",
    # Who you are
    'author': "jac",
    'website': "http://localhost:8069/web",

    # categories can be used to filter modules in modules listing
    'category': 'web',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],
    'data': ['views/blog_views.xml'],
    
    'tests': [
    ],
}
