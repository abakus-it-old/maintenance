# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class AccessRights(models.Model):
    _name = 'security.check.access.rights'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    username = fields.Char(string='User Name', required=True)
    groups = fields.Char(required=True)
    shares = fields.Char(required=True)
    rights = fields.Char(required=True)
