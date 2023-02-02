from datetime import timedelta

from odoo import api, fields, models

class Mission(models.Model):
    _name = 'mision_espacial.mission'
    _description = "Space Missions"
    
    
    active = fields.Boolean(default=True)
    name = fields.Char(name='Mission Name')
    priority = fields.Selection(selection=[("1","1"),
                                          ("2","2"),
                                          ("3","3"),
                                          ("4","4"),
                                          ("5","5"),])
    
    type = fields.Selection(selection=[('supply_delivery','Supply Delivery'),
                                   ('exploration', 'Exploration'),
                                   ('war_efforts', 'War Efforts'),
                                   ('transport', 'Transportation')],
                        string='Mission Type',)
    
    launch_date = fields.Datetime(string="Launch Date",
                                  default=fields.Date.today)
    duration = fields.Float(string='Duration',
                           default="1")
    return_date = fields.Datetime(string="Return Date",
                          compute='_compute_return_date',
                          inverse='_inverse_return_date',
                          store=True)
    
    spaceship_id = fields.Many2one(comodel_name='mision_espacial.spaceship')
    
    @api.depends('launch_date', 'duration')
    def _compute_return_date(self):
        for record in self:
            if not (record.launch_date and record.duration):
                record.return_date = record.launch_date
            else:
                duration = timedelta(days=record.duration)
                record.return_date = record.launch_date + duration
    
    def _inverse_return_date(self):
        for record in self:
            if record.launch_date and record.return_date:
                record.duration = (record.return_date - record.launch_date).days
            else:
                continue