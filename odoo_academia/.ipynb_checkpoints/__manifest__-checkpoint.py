# -*- coding:utf-8 -*-

{
    'name' : 'Academia Odoo',
    
    'summary': """Aplicacion Academia - ODOO Training""",
    
    'description': """
        Modulo para manejar Entrenamiento:
        - Cursos
        - Sesiones
        -
     """,
    
    'author:' : 'Rodrigo Suarez',
    
    'website' : 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/ir.model.access.csv',
        'security/academia_seguridad.xml'
    ],
    
    'demo': [ 'demo/academy_demo.xml',
    
    ],
     #Add license to remove License Warning
    'license': 'OPL-1'
}