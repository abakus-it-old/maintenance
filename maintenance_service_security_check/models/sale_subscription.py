    # -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class Subscription(models.Model):
    _inherit = ['sale.subscription']

    security_check_ids = fields.One2many('security.check', 'subscription_id', string='Security Checks')
    security_check_count = fields.Integer(string="Security Checks Count", compute='_compute_security_check_count')

    @api.one
    def _compute_security_check_count(self):
        self.security_check_count = len(self.security_check_ids)