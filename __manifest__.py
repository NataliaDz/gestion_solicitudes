# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Solicitudes',
    'version': '19.0.1.0.0',
    'category': 'Gestión Interna',
    'summary': 'Módulo para gestionar solicitudes internas (IT, RRHH, Compras)',
    'description': """
        Módulo personalizado para gestionar solicitudes internas de la empresa.
        Permite registrar y hacer seguimiento de solicitudes en las áreas de:
        - IT (Soporte técnico, incidencias, proyectos)
        - RRHH (Vacaciones, nóminas, certificados)
        - Compras (Pedidos, proveedores)
    """,
    'author': 'Tu Empresa',
    'website': 'https://www.tuempresa.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/solicitud_menu.xml',
        'views/solicitud_views.xml',
        'data/solicitud_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}