# -*- coding: utf-8 -*-
{
    'name': 'Mobile Shop Management',
    'version': '14.0',
    'summary': 'Odoo 14 Development by student',
    'sequence': -100,
    'description': """Odoo 14 Development""",
    'category': 'Productivity',
    'author': 'Group 8',
    'maintainer': 'Group 8',
    'website': 'https://www.due.udn.vn',
    'license': 'LGPL-3',
    'depends': ['sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/lot_serial.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
