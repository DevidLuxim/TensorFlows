# -*- coding: utf-8 -*-
{
    'name': "Image recognizer",

    'summary': "Image recognizer",

    'author': "Luxim",
    'website': "https://www.luxim.si",
    'license': 'LGPL-3',
    'version': '0.1',
    'category': 'AI',
    'images': ["static/description/thumbnail.png"],
    'price': 4.99,
    'currency': 'EUR',

    # any module necessary for this one to work co¸rrectly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/image_recognizer.xml',
    ],
}
