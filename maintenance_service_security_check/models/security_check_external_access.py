# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class ExternalAccess(models.Model):
    _name = 'security.check.external.access'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    username = fields.Char(string='User Name', required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    connection_mode = fields.Char(required=True)
