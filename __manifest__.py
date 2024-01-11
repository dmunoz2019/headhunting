# -*- coding: utf-8 -*-
{
    'name': "headhunting",

    'summary': "headhunting",

    'description': """
headhunting    """,

    'author': "datakraft",
    'website': "https://datakraftguatemala.com/",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_recruitment','hr_contract','hr','documents','mail','sale_subscription'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hh_candidate.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'headhunting/static/src/components/*/*.js',
            'headhunting/static/src/components/*/*.xml',
            'headhunting/static/src/components/*/*.scss',
        ],
    },
}

