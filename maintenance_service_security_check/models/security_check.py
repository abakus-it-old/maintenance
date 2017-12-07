# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class SecurityCheck(models.Model):
    _name = 'security.check'
    _order = 'date_end'
    # _inherit = 'mail.thread'

    name = fields.Char(string='Description', index=True, required=True, readonly=True, states={'running': [('readonly', False)]}, track_visibility='always')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('waiting', 'Waiting validation'),
        ('closed', 'Closed'),
        ('cancel', 'Cancelled'),
    ], string='State', default='draft', required=True, track_visibility='always')
    date_end = fields.Date(string='End Date', required=True, readonly=True, states={'running': [('readonly', False)]})
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, readonly=True, states={'running': [('readonly', False)]})

    external_access_ids = fields.One2many('security.check.external.access', 'check_id', string="External Accesses", readonly=True, states={'running': [('readonly', False)]})
    external_access_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    external_access_check_date = fields.Date(string='Check Date')

    backup_ids = fields.One2many('security.check.backup', 'check_id', string="Backups", readonly=True, states={'running': [('readonly', False)]})
    backup_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    backup_check_date = fields.Date(string='Check Date')

    access_rights_ids = fields.One2many('security.check.access.rights', 'check_id', string="Access Rights", readonly=True, states={'running': [('readonly', False)]})
    access_rights_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    access_rights_check_date = fields.Date(string='Check Date')

    gate_access_ids = fields.One2many('security.check.gate.access', 'check_id', string="Gate Accesses", readonly=True, states={'running': [('readonly', False)]})
    gate_access_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    gate_access_check_date = fields.Date(string='Check Date')

    server_security_ids = fields.One2many('security.check.server.security', 'check_id', string="Servers Security", readonly=True, states={'running': [('readonly', False)]})
    server_security_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    server_security_check_date = fields.Date(string='Check Date')

    network_security_ids = fields.One2many('security.check.network.security', 'check_id', string="Network Security", readonly=True, states={'running': [('readonly', False)]})
    network_security_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    network_security_check_date = fields.Date(string='Check Date')

    workstation_security_ids = fields.One2many('security.check.workstation.security', 'check_id', string="Workstations Security", readonly=True, states={'running': [('readonly', False)]})
    workstation_security_attachment_ids = fields.Many2many('ir.attachment', string='Signed Report')
    workstation_security_check_date = fields.Date(string='Check Date')

    @api.multi
    def action_confirm(self):
        self.state = 'open'

    @api.multi
    def action_done(self):
        self.state = 'waiting'

    @api.multi
    def action_validate(self):
        self.state = 'closed'

    @api.multi
    def action_cancel(self):
        self.state = 'cancel'

    @api.multi
    def action_redraft(self):
        self.state = 'draft'
    
    @api.multi
    def print_access_rights(self):
        return self.env['report'].get_action(self, 'maintenance_service_security_check.report_access_rights_template')