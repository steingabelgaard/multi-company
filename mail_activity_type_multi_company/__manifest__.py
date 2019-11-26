# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Mail Activity Type Multi Company',
    'version': '12.0.1.0.1',
    'license': 'AGPL-3',
    'author': 'Stein & Gabelgaard ApS,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/multi-company',
    'depends': ['mail'],
    'post_init_hook': 'post_init_hook',
    'data': [
        'security/mail_activity_type.xml',
        'views/mail_activity_type.xml'
    ],
    'development_status': 'Beta',
    
}
