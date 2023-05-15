
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class CarRentalDriver(models.Model):
    _name = 'car.rental.drivers'
    _description = 'Car Rental Drivers'

    name = fields.Char(string='Driver Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    license_number = fields.Char(string='Driver License Number', required=True) 
    license_expiration_date = fields.Date(string='Driver License Expiration Date', required=True)
    