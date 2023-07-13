{
    'name': "Isha Meditator",
    'version': '15.0.0.0.1',
    'license': 'LGPL-3',
    'summary': "Isha Meditator",
    'complexity': "easy",
    'author': 'Isha Foundation',
    'website': 'https://ishafoundation.org',
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/data_isha_programs.xml',

        'views/isha_meditator.xml',
        'views/isha_program.xml',
        'views/isha_volunteer.xml',
        'wizard/volunteer_wizard.xml',
        'menus/menus.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
