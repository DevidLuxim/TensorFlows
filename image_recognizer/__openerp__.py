# -*- coding: utf-8 -*-
{
    'name': "Image recognizer",

    'summary': "Image recognizer",

    'description': "Module that recognize photos using Tensor Flow library",

    'author': "Luxim",
    'website': "https://www.luxim.si",
    'version': '0.1',
    'category': 'AI',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/image_recognizer.xml',
    ],
}