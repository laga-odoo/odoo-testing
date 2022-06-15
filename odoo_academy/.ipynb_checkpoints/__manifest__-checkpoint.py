# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage training""",
    'description': 'yup',
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.2',
    'depends': ['base'],
    'data': [ # loads the files in order
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'data/academy_demo.xml',
        
    ],
    'demo': [
        #'demo/academy_demo.xml',
        
    ],
}