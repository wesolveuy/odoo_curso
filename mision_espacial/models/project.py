# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Project(models.Model):
    _inherit = "project.project"
    
    mission_id = fields.Many2one(comodel_name='mision_espacial.mission',
                                 string="Mission")
    user_id = fields.Many2one(string='Mission Captain')