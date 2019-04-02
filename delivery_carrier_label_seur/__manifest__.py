# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# © 2017 PESOL - Angel Moya <angel.moya@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Seur Deliveries WebService",
    "summary": "Allows to generate shipping label for SEUR shipments.",
    "version": "10.0.1.0.0",
    "category": "Delivery",
    "website": "http://factorlibre.com",
    "author": "FactorLibre, PESOL, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": ['seur', 'unidecode'],
    },
    "depends": [
        "delivery",
        "base_delivery_carrier_label",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/seur_config_view.xml",
        "views/delivery_view.xml",
        "views/stock_view.xml"
    ],
    "demo": [],
    "qweb": []
}
