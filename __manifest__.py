# -*- coding: utf-8 -*-

## Agira Technologies

{
    'name': "Products Wishlist Feature",
    'version': '13',
    'summary': """Enabled the Wishlist feature in Ecommerce website.""",
    'description': """This module will enable the wishlist feature in website setting and record the products """,
    'author': "Agira Technologies",
    'website': "https://www.agiratech.com/",
    'category': 'Website',
    'depends': [
        'website_sale_wishlist',
    ],
    'data': [
        'views/product_wishlist_feature_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}