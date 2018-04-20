# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class ServerSecurity(models.Model):
    _name = 'security.check.server.security'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    server = fields.Char(required=True)
    hardware_ok = fields.Boolean(string='Hardware OK')
    maintenance = fields.Boolean(string='Apps & OS Maintenance')
    shadow_copies = fields.Boolean(string='Shadow Copies Turned On')
    resources_ok = fields.Boolean(string='Resources OK')
    irmc_ok = fields.Boolean(string='IRMC OK')
    monitoring_probes = fields.Text(required=True)
