# -*- coding: utf-8 -*-
# (c) 2018 AbAKUS IT SOLUTION

import logging
from openerp import models, fields, api
_logger = logging.getLogger(__name__)


class ResPartnerUsername(models.Model):
    _inherit = 'res.partner'

    username = fields.Char(string="Login")
