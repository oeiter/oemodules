# -*- coding: utf-8 -*-
from openerp.osv import orm, fields
import logging

_logger = logging.getLogger(__name__)

class blog_category(orm.Model):
    _name = "simpleblog.category"
    _columns = {
        'name': fields.char(string="Category", required=True, translate=True),
    }
class blog_details(orm.Model):
    _name = "simpleblog.blogdetails"

    _order = 'title asc'

    _columns = {
        'title': fields.char(string="Title", size=15,required=True, translate=True),
        'category': fields.many2one("simpleblog.category","Category", required=True),
        'content': fields.text('Your blog text'),
    }
    _defaults = {
    }
    _sql_constraints = []
    
    def get_blog_from_details(self, cr, uid, task_ids, context=None):
        return ("abc")

