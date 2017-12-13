# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class AnalyticLine(models.Model):
    _inherit = ['account.analytic.line']

    security_check_id = fields.Many2one('security.check', string='Security Check')