# -*- coding: utf-8 -*-
from openerp.osv import orm, fields
import logging

_logger = logging.getLogger(__name__)

class whoami_info(orm.Model):
    _name = "whoami.info"

    _order = 'name asc'

    _columns = {
        'name': fields.char(string="Name", required=True, translate=True),
        'start_date': fields.date('Date'),
        'days': fields.integer('Leave days'),
        'reason': fields.text('Leave Reason Information'),
    }
    _defaults = {
        'days': 0,
    }
    _sql_constraints = [
        ('positive_days', 'CHECK(days >= 0)', 'Days number MUST be a positive')
    ]
