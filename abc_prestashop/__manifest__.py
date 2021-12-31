# -*- coding: utf-8 -*-
{
    'name': "A.B.C. Prestashop Connector",
    'summary': """ Modulo connettore che contiene le funzioni per l'interscambio dati verso Prestashop. """,
    'description': """ Modulo connettore che contiene le funzioni per l'interscambio dati verso Prestashop. """,
    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",
    'category': 'API',
    'version': '1.0',
    'depends': ['base', 'sale', 'sale_management', 'pos_sale', 'sale_enterprise', 'sale_margin', 'sale_stock', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [],
    "installable": True,
    'application': True,
}
