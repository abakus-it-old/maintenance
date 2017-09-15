# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class AccessRights(models.Model):
    _name = 'security.check.access.rights'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    username = fields.Char(string='User Name', required=True)
    groups = fields.Char(string='Groups', required=True)
    shares = fields.Char(string='Shares', required=True)
    rights = fields.Char(string='Rights', required=True)