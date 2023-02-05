# -*- coding: utf-8 -*-

from odoo import models, field, api

class Curso(models.Model):
    _name:'academia.curso'
    _description:'Info Curso'
    
    nombre=fields.Char(string='Titulo',required='True')
    descripcion = field.Text(string='Descripcion')
    
    nivel = fields.Selection(string='Nivel',
                             selection=[('basico','Basico'),
                                        ('intermedio','Intermedio'),
                                        ('avanzado','Avanzado')],
                             copy='false')