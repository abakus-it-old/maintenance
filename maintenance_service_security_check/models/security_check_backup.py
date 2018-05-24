# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class Backup(models.Model):
    _name = 'security.check.backup'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    source = fields.Char(required=True)
    destination = fields.Char(required=True)
    frequency = fields.Char(required=True)
    date_last_successful_restore = fields.Date(string='Last Successful Restore', required=True)
    report_monitoring = fields.Char(required=True)
    type_id = fields.Many2one('backup.type', string="Type", required=True)
