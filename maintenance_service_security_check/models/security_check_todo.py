# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, exceptions, _
_logger = logging.getLogger(__name__)


class Todo(models.Model):
    _name = 'security.check.todo'

    check_id = fields.Many2one('security.check', string='Security Check', required=True)
    name = fields.Char(required=True)
    description = fields.Text()
    issue_id = fields.Many2one('project.issue', string="Issue")
    issue_state_id = fields.Many2one(related='issue_id.stage_id', string="Issue State")
