# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class WorkstationSecurity(models.Model):
    _name = 'security.check.workstation.security'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    workstation = fields.Char(required=True)
    antivirus_ok = fields.Boolean(string='Antivirus OK')
