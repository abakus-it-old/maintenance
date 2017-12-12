# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class NetworkSecurity(models.Model):
    _name = 'security.check.network.security'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    firewall = fields.Char(string='Firewall', required=True)
    firewall_licences_ok = fields.Boolean(string='Firewall Licenses OK')
    firewall_rules_ok = fields.Boolean(string='Firewall Rules OK')
    wlan = fields.Char(string='WLAN', required=True)
    complex_passwords = fields.Boolean(string='Complex Passwords')