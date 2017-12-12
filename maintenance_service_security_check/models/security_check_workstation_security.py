# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class WorkstationSecurity(models.Model):
    _name = 'security.check.workstation.security'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    workstation = fields.Char(string='Workstation', required=True)
    antivirus_ok = fields.Boolean(string='Antivirus OK')