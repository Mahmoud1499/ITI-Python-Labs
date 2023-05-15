# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarRentalCar(models.Model):
    _name = 'car.rental.cars'
    _description = 'Car Rental Cars'

    name = fields.Char(string='Car Manufacturer', required=True, default='BMW')
    active = fields.Boolean(string='Active', default=True)
    model = fields.Char(string='Car Model', required=True)
    color = fields.Selection(selection=[
        ('red', 'Red'), 
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ], string='Car Color', required=True)
    license_plate = fields.Char(string='Car License Plate', required=True)
    license_expiration_date = fields.Date(string='Car License Expiration Date', required=True)
    year = fields.Integer(string='Car Year', required=True)
    price = fields.Float(string='Car Price', required=True)
    image = fields.Image(string='Car Image', required=True)
    note = fields.Text(string='Car Note')
    sale_ids = fields.One2many(comodel_name='car.rental.sales', inverse_name='car', string='Sales')



