# -*- coding: utf-8 -*-
# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, fields, _
from odoo.exceptions import UserError


class ZipcodeSelectorWizard(models.TransientModel):
    _name = 'zipcode.selector.wizard'

    @api.model
    def _get_default_partner_id(self):
        if 'partner_id' not in self._context:
            raise UserError(_())
        return self._context.get('partner_id')

    @api.model
    def _get_default_picking_id(self):
        if 'picking_id' not in self._context:
            raise UserError(_())
        return self._context.get('picking_id')

    @api.model
    def _get_default_zip_options(self):
        if 'zip_data' not in self._context:
            return []
        default_zip_options = []
        for zipcode in self._context.get('zip_data'):
            default_zip_options.append(
                (zipcode['NOM_POBLACION'], zipcode['NOM_POBLACION']))
        return default_zip_options

    picking_id = fields.Many2one(
        'stock.picking', 'Customer',
        default=lambda self: self._get_default_picking_id())
    partner_id = fields.Many2one(
        'res.partner', 'Customer',
        default=lambda self: self._get_default_partner_id())
    partner_city = fields.Char(
        'Delivery city', related='partner_id.city', readonly=True)
    city_name = fields.Selection(
        lambda self: self._get_default_zip_options(), string='Seur city')

    def confirm(self):
        self.partner_id.city = self.city_name
        context = dict(self.env.context)
        context['zip_checked_%s' % self.partner_id.id] = True
        return self.picking_id.with_context(context).action_generate_carrier_label()
