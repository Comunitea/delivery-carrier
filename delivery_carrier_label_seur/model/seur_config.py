# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields


class SeurConfig(models.Model):
    _name = 'seur.config'

    name = fields.Char(required=True)
    vat = fields.Char('VAT', required=True)
    integration_code = fields.Char(required=True)
    accounting_code = fields.Char(required=True)
    franchise_code = fields.Char(required=True)
    username = fields.Char(required=True)
    password = fields.Char(required=True)
    file_type = fields.Selection([
        ('pdf', 'PDF'),
        ('txt', 'TXT')
    ], required=True)
