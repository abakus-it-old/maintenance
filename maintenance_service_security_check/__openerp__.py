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

        'report/layouts.xml',
        'report/external_access_template.xml',
        'report/backups_template.xml',
        'report/access_rights_template.xml',
        'report/gate_access_template.xml',
        'report/servers_security_template.xml',
        'report/network_security_template.xml',
        'report/workstations_security_template.xml',
        'report/reports.xml',
    ],
    'application': True
}
