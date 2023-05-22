
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class CarRentalDealers(models.Model):
    _name = 'car.rental.dealers'
    _description = 'Car Rental dealers'

    name = fields.Char(string='Dealers Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    license_number = fields.Char(string='Dealers License Number', required=True) 
    license_expiration_date = fields.Date(string='Dealers License Expiration Date', required=True)
    