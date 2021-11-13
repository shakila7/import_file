# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Import Documents',
    'version' : '1.1',
    'summary': 'Import Documents to sale order',
    'sequence': 10,
    'description': """
        Import Documents to sale order
    """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : ['sale_management','account'],
    'data': [
        'security/ir.model.access.csv',
        'security/file_security.xml',
        'views/import_file_sale_order_inherit_view.xml',
        'views/approve_file_account_move_inherit.xml',
        
        
    ],
    'demo': [
       
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
