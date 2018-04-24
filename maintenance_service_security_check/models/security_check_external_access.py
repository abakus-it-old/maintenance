# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class ExternalAccess(models.Model):
    _name = 'security.check.external.access'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    partner_id = fields.Many2one('res.partner', string="User", required=True)
    # username = fields.Char(relate='partner_id.username', string='User Name', readonly=True)
    connection_mode_ids = fields.Many2many('connection.mode', string="Connection Mode")
    comment = fields.Char()
