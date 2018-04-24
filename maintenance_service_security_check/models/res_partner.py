# -*- encoding: utf-8 -*-
# (c) 2018 AbAKUS IT SOLUTION

from openerp import models, fields, api


class ResPartnerUsername(models.Model):
    _inherit = 'res.partner'

    username = fields.Char(string="Logging", store=True)
