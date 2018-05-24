# -*- coding: utf-8 -*-

import logging
from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
_logger = logging.getLogger(__name__)


class SecurityCheck(models.Model):
    _name = 'security.check'
    _inherit = ['mail.thread']
    _order = 'date_end'

    name = fields.Char(string='Titre', index=True, required=True, track_visibility='always', compute='_compute_name')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('waiting', 'Waiting validation'),
        ('closed', 'Closed'),
        ('cancel', 'Cancelled'),
    ], default='draft', required=True, track_visibility='always')
    date_end = fields.Date(string='End Date', required=True, readonly=True, states={'draft': [('readonly', False)]})
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, readonly=True,
                                 states={'draft': [('readonly', False)]})
    subscription_id = fields.Many2one('sale.subscription', string='Contract', readonly=True,
                                      states={'draft': [('readonly', False)]})
    analytic_account_id = fields.Many2one(string="Account", related='subscription_id.analytic_account_id')
    timesheet_line_ids = fields.One2many('account.analytic.line', 'security_check_id', string="Timesheet lines", )

    external_access_ids = fields.One2many('security.check.external.access', 'check_id', string="External Accesses",
                                          readonly=True, states={'open': [('readonly', False)]})
    external_access_attachment_ids = fields.Many2many('ir.attachment', 'ea_attachment_id', string='Signed Report')
    external_access_check_date = fields.Date(string='Check Date')
    external_access_free_text = fields.Text(string="Comments on External Access")

    backups_ids = fields.One2many('security.check.backup', 'check_id', string="Backups", readonly=True,
                                  states={'open': [('readonly', False)]})
    backups_attachment_ids = fields.Many2many('ir.attachment', 'ba_attachment_id', string='Signed Report')
    backups_check_date = fields.Date(string='Check Date')
    backups_free_text = fields.Text(string="Comments on Backups")

    access_rights_ids = fields.One2many('security.check.access.rights', 'check_id', string="Access Rights",
                                        readonly=True, states={'open': [('readonly', False)]})
    access_rights_attachment_ids = fields.Many2many('ir.attachment', 'ar_attachment_id', string='Signed Report')
    access_rights_check_date = fields.Date(string='Check Date')
    access_rights_free_text = fields.Text(string="Comments on Access Rights")

    gate_access_ids = fields.One2many('security.check.gate.access', 'check_id', string="Gate Accesses",
                                      readonly=True, states={'open': [('readonly', False)]})
    gate_access_attachment_ids = fields.Many2many('ir.attachment', 'ga_attachment_id', string='Signed Report')
    gate_access_check_date = fields.Date(string='Check Date')
    gate_access_free_text = fields.Text(string="Comments on Gate Access")

    server_security_ids = fields.One2many('security.check.server.security', 'check_id', string="Servers Security",
                                          readonly=True, states={'open': [('readonly', False)]})
    server_security_attachment_ids = fields.Many2many('ir.attachment', 'ss_attachment_id', string='Signed Report')
    server_security_check_date = fields.Date(string='Check Date')
    server_security_free_text = fields.Text(string="Comments on Server Security")

    network_security_ids = fields.One2many('security.check.network.security', 'check_id', string="Network Security",
                                           readonly=True, states={'open': [('readonly', False)]})
    network_security_attachment_ids = fields.Many2many('ir.attachment', 'ns_attachment_id', string='Signed Report')
    network_security_check_date = fields.Date(string='Check Date')
    network_security_free_text = fields.Text(string="Comments on Network Security")

    workstation_security_ids = fields.One2many('security.check.workstation.security', 'check_id',
                                               string="Workstations Security", readonly=True,
                                               states={'open': [('readonly', False)]})
    workstation_security_attachment_ids = fields.Many2many('ir.attachment', 'ws_attachment_id', string='Signed Report')
    workstation_security_check_date = fields.Date(string='Check Date')
    workstation_security_free_text = fields.Text(string="Comments on Workstation Security")

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
    def action_refuse(self):
        self.state = 'open'

    @api.multi
    def action_cancel(self):
        self.state = 'cancel'

    @api.multi
    def action_redraft(self):
        self.state = 'draft'

    @api.multi
    def action_duplicate(self):
        for check in self:
            new_check_id = check.copy(default={'partner_id': check.partner_id.id, 'state': 'draft'})
            return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'res_model': 'security.check',
                'view_mode': 'form',
                'res_id': new_check_id.id,
                'target': 'current',
            }

    @api.multi
    @api.depends('partner_id', 'date_end')
    def _compute_name(self):
        for check in self:
            check.name = "SC - %s - %s" % (check.partner_id.name, check.date_end)

    @api.multi
    def print_external_access(self):
        return self.env['report'].get_action(self, 'maintenance_service_security_check.report_external_access_template')

    @api.multi
    def print_backups(self):
        return self.env['report'].get_action(self, 'maintenance_service_security_check.report_backups_template')

    @api.multi
    def print_access_rights(self):
        return self.env['report'].get_action(self, 'maintenance_service_security_check.report_access_rights_template')

    @api.multi
    def print_gate_access(self):
        return self.env['report'].get_action(self, 'maintenance_service_security_check.report_gate_access_template')

    @api.multi
    def print_servers_security(self):
        return self.env['report'].get_action(self,
                                             'maintenance_service_security_check.report_servers_security_template')

    @api.multi
    def print_network_security(self):
        return self.env['report'].get_action(self,
                                             'maintenance_service_security_check.report_network_security_template')

    @api.multi
    def print_workstations_security(self):
        return self.env['report'].get_action(self,
                                             'maintenance_service_security_check.report_workstations_security_template')

    @api.multi
    def import_gate_access_users(self):
        # is company set ?
        if not self.partner_id:
            return ValidationError(_("Please set a Customer first"))

        if len(self.gate_access_ids) > 0:
            return ValidationError(_("Please empty user list first"))

        # get all company contacts, filter by in_portal
        users = self.env['res.users'].search([
            '|',
            ('partner_id.parent_id', '=', self.partner_id.id),
            ('partner_id', '=', self.partner_id.id)
        ])

        for user in users:
            # look for associated user
            #user = self.env['res.users'].search([('partner_id', '=', partner.id)])
            self.gate_access_ids.create({
                'check_id': self.id,
                'username': user.partner_id.name,
                'sales_ku': user.partner_id.keyuser_sales,
                'accounting_ku': user.partner_id.keyuser_accounting,
                'project_ku': user.partner_id.keyuser_project,
                'date_last_connection': user.login_date or _('never connected'),
            })
        return

    @api.multi
    def action_print_complete(self):
        return self.env['report'].get_action(self,
                                             'maintenance_service_security_check.security_check_report_complete_template')
