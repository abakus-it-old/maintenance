# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class ConfigConnectionMode(models.Model):
    _name = 'connection.mode'
    _order = 'name'

    name = fields.Char()
    active = fields.Boolean(default=True)
    description = fields.Char()
