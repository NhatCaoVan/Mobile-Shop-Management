# -*- coding: utf-8 -*-

{
    "name": "Mobile Shop",
    "summary": """Module develop by group 8
       """,
    'sequence': -10,
    'category': 'Productivity',
    "version": "14.0.1.0.2",
    'license': 'LGPL-3',
    "author": "G8",
    "website": "https://github.com/NhatCaoVan/Mobile-Shop-Management.git",
    "depends": ['sale', 'stock', "sale_management", "delivery", 'base', "account"],
    "data": ["views/sale_view.xml",
             "views/lot_serial.xml",
             "views/product.xml",
             "views/product_template.xml",
             "report/sale_report_inherit.xml"


             ],
    "post_init_hook": "set_sale_price_on_variant",
    'demo': [],
    'qweb': [],
    'images': ['static/description/ff.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

