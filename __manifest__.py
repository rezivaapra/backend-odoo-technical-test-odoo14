{
    'name': 'Material Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Module for managing materials',
    'description': """
        This module allows the registration and management of materials, including CRUD operations and filtering.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/supplier_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}