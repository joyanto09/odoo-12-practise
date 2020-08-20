{
    'name': 'Odoo 12 Practise Work For Git',
    'summary': """This module will Practise""",
    'version': '1.0.0.0',
    'description': """This module will test work

        By Joyanto Git """,
    'author': 'Metamorphosis',
    'company': 'Metamorphosis Ltd.',
    'website': 'http://www.metamorphosis.com.bd',
    'category': 'Extra Tools',
    'depends': ['base', 'sale'],
    'licence': 'OPL-1',
    'data': [
        'security/ir.model.access.csv',

        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/server_action.xml',
        # 'data/data_home.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,
}