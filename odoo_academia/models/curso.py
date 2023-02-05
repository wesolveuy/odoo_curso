# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Curso(models.Model):
    _name:'academia.curso'
    _description:'Info Curso'
    
    nombre=fields.Char(string='Titulo',required='True')
    descripcion = fields.Text(string='Descripcion')
    
    nivel = fields.Selection(string='Nivel',
                             selection=[('basico','Basico'),
                                        ('intermedio','Intermedio'),
                                        ('avanzado','Avanzado')],
                             copy='false')
    
    activo = fields.Boolean(string='Activo',default='True')