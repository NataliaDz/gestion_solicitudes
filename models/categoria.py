# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Categoria(models.Model):
    _name = 'gestion_solicitudes.categoria'
    _description = 'Categoría de Solicitud'
    _order = 'name asc'

    name = fields.Char(string='Nombre', required=True, translate=True)
    codigo = fields.Char(string='Código', required=True)
    descripcion = fields.Text(string='Descripción')
    active = fields.Boolean(string='Activo', default=True)

    _sql_constraints = [
        ('codigo_uniq', 'unique(codigo)', 'El código de categoría debe ser único.')
    ]