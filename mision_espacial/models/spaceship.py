from odoo import api, fields, models
from odoo.exceptions import ValidationError,UserError

class Spaceship(models.Model):

    _name = 'mision_espacial.spaceship'
    _description = "Space Mission Spaceship"
    
    #Fields definition
    name = fields.Char(string='Vessel Name')
    active = fields.Boolean(default=True)    
    type = fields.Selection(selection=[('freighter','Freighter'),
                                       ('star_destroyer', 'Star Destroyer'),
                                       ('star_cruiser', 'Star Destroyer'),
                                       ('x_wing', 'X-Wing Fighter')],
                            string='Ship Type',)
    model = fields.Char(string='Ship Model', 
                        required = True)
    capacity_passenger = fields.Integer(string= "Number of Passengers",
                                        help="Maximum number of passengers in the Spaceship",)
    length = fields.Float(help="Length of the Ship",)
    width = fields.Float(help="Width of the Ship",)
    height = fields.Float(help="Height of the Ship",)
    weight = fields.Float(string="Empty Weight",
                                        help="Weight of the ship without fuel, passengers or cargo",)
    fuel_type = fields.Selection(selection=[('solid_fuel','Solid Fuel'),
                                            ('liquid_fuel', 'Liquid Fuel')],
                                 string='Fuel Type',)
    
    crew_ids = fields.Many2many(comodel_name='res.partner',
                            string='Crew')
    mission_ids = fields.One2many(comodel_name='mision_espacial.mission',
                               inverse_name='spaceship_id')
            

    @api.onchange('capacity_passenger','length')
    def _onchange_dimensions(self):
        if self.capacity_passenger<=0:
            raise UserError('La cantidad de pasajeros debe ser mayor que 0')
        if self.length<=0:
            raise UserError('El largo no puede ser menor que 0')
            
    @api.constrains('width','length')
    def _check_width_less_length(self):
        for record in self:
            if record.width > record.length:
                raise ValidationError(('Hey! The width can not be bigger than the length.')) 