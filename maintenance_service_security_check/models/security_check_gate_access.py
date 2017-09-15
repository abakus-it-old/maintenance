# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class GateAccess(models.Model):
    _name = 'security.check.gate.access'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    username = fields.Char(string='User Name', required=True)
    sales_ku = fields.Boolean(string='Sales KU')
    accounting_ku = fields.Boolean(string='Accounting KU')
    project_ku = fields.Boolean(string='Project KU')
    date_first_connection = fields.Date(string='First Connection', required=True)