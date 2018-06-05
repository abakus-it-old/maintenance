# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class ConfigBackupType(models.Model):
    _name = 'backup.type'
    _order = 'name'

    name = fields.Char()
    active = fields.Boolean(default=True)
    description = fields.Char()
