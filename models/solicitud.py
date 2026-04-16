# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta


class Solicitud(models.Model):
    _name = 'gestion_solicitudes.solicitud'
    _description = 'Solicitud'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Título', required=True, tracking=True)
    categoria_id = fields.Many2one(
        'gestion_solicitudes.categoria',
        string='Categoría',
        required=True,
        tracking=True,
        domain=[('active', '=', True)]
    )
    solicitante_id = fields.Many2one(
        'res.users',
        string='Solicitante',
        required=True,
        default=lambda self: self.env.user,
        tracking=True
    )
    descripcion = fields.Text(string='Descripción', tracking=True)
    prioridad = fields.Selection(
        [
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta'),
            ('urgente', 'Urgente'),
        ],
        string='Prioridad',
        default='media',
        tracking=True
    )
    estado = fields.Selection(
        [
            ('borrador', 'Borrador'),
            ('pendiente', 'Pendiente de revisión'),
            ('asignado', 'Asignado'),
            ('en_proceso', 'En proceso'),
            ('espera', 'En espera de información'),
            ('resuelto', 'Resuelto'),
            ('cerrado', 'Cerrado'),
            ('rechazado', 'Rechazado'),
        ],
        string='Estado',
        default='borrador',
        tracking=True
    )
    asignado_id = fields.Many2one(
        'res.users',
        string='Asignado a',
        tracking=True
    )
    fecha_solicitud = fields.Datetime(
        string='Fecha de Solicitud',
        default=fields.Datetime.now,
        required=True
    )
    fecha_prevista = fields.Date(string='Fecha Prevista')
    fecha_resolucion = fields.Datetime(string='Fecha de Resolución', copy=False)
    adjunto = fields.Binary(string='Adjunto', attachment=True)
    adjunto_filename = fields.Char(string='Nombre del Adjunto')
    notas = fields.Text(string='Notas Internas')
    company_id = fields.Many2one(
        'res.company',
        string='Empresa',
        default=lambda self: self.env.company,
        required=True
    )

    _sql_constraints = [
        ('name_categoria_uniq', 'unique(name, categoria_id)',
        'Ya existe una solicitud con este nombre en la misma categoría.')
    ]

    def action_borrador(self):
        self.write({'estado': 'borrador'})

    def action_pendiente(self):
        self.write({'estado': 'pendiente'})

    def action_asignar(self):
        self.write({'estado': 'asignado'})

    def action_en_proceso(self):
        self.write({'estado': 'en_proceso'})

    def action_espera(self):
        self.write({'estado': 'espera'})

    def action_resolver(self):
        self.write({
            'estado': 'resuelto',
            'fecha_resolucion': fields.Datetime.now()
        })

    def action_cerrar(self):
        self.write({'estado': 'cerrado'})

    def action_rechazar(self):
        self.write({'estado': 'rechazado'})

    def action_reabrir(self):
        self.write({
            'estado': 'en_proceso',
            'fecha_resolucion': False
        })

    def _get_default_repartidor_destinatario(self):
        return self.env.user.email

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].strip()
        return super(Solicitud, self).create(vals)

    def write(self, vals):
        if 'estado' in vals:
            if vals['estado'] in ['cerrado', 'rechazado'] and self.estado not in ['cerrado', 'rechazado']:
                if not self.fecha_resolucion:
                    vals['fecha_resolucion'] = fields.Datetime.now()
        return super(Solicitud, self).write(vals)

    @api.constrains('fecha_prevista')
    def _check_fecha_prevista(self):
        for record in self:
            if record.fecha_prevista and record.fecha_prevista < fields.Date.today():
                raise ValidationError('La fecha prevista no puede ser anterior a hoy.')