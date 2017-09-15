{
    'name': "Security Check",
    'version': '9.0.1.0',
    'depends': [
        'base'
    ],
    'author': "Jason PINDAT @ AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Other',
    'description': """
        Security Check

        Adds a security checklist system

        This module has been developed by Jason PINDAT @ AbAKUS it-solutions.
    """,
    'data': [
        'views/menu_buttons.xml',
        'views/security_check.xml',
        # 'security/ir.model.access.csv',

        'report/layout.xml',
        'report/access_rights_template.xml',
        'report/reports.xml',
    ],
    'application': True
}
