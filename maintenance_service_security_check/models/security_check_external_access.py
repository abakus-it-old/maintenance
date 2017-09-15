# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class ExternalAccess(models.Model):
    _name = 'security.check.external.access'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    username = fields.Char(string='User Name', required=True)
    firstname = fields.Char(string='First Name', required=True)
    lastname = fields.Char(string='Last Name', required=True)
    connection_mode = fields.Char(string='Connection Mode', required=True)