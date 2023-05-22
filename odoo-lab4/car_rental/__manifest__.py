# -*- coding: utf-8 -*-
{
    'name': "Car Rental Module",

    'summary': """
        ITI Car Rental Module""",

    'description': """
        ITI Car Rental Module
    """,

    'author': "My Company",
    'website': "https://www.iti.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cars.xml',
        'views/rental_inherit.xml',
        'views/drivers.xml',
        'views/dealers.xml',
        'views/sales.xml',
        'views/templates.xml',
        'car_rental_report.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
