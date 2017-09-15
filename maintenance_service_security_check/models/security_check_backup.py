# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class Backup(models.Model):
    _name = 'security.check.backup'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    source = fields.Char(string='Source', required=True)
    destination = fields.Char(string='Destination', required=True)
    frequency = fields.Char(string='Frequency', required=True)
    date_last_successful_restore = fields.Date(string='Last Successful Restore', required=True)
    report_monitoring = fields.Char(string='Report Monitoring', required=True)