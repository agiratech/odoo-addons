# -*- coding: utf-8 -*-

## Agira Technologies

{
    'name': "Products Wishlist Feature",
    'version': '10',
    'summary': """Created the Wishlist feature in Ecommerce website.""",
    'description': """This module will create the wishlist feature in website products sale and record the products """,
    'author': "Agira Technologies",
    'website': "https://www.agiratech.com/",
    'category': 'Website',
    'depends': [
        'website_sale',
    ],
    'data': [
        "security/ir.model.access.csv",
        "security/ir.rule.csv",
        "data/ir_cron.yml",
        "views/assets.xml",
        "views/layout.xml",
        "views/shop.xml",
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}