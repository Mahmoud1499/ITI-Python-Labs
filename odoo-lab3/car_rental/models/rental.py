
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarRentalSales(models.Model):
    _name = 'car.rental.sales'
    _description = 'Car Rental Sales'

    name = fields.Char(string='Sales Number', required=True)
    car = fields.Many2one(comodel_name='car.rental.cars', string='Car', required=True)
    driver = fields.Many2one(comodel_name='car.rental.drivers', string='Driver', required=True)
    date = fields.Date(string='Date', required=True)
    price = fields.Float(string='Price', required=True)
    customer = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    
  duration = fields.Integer(string='Duration (Days)')
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    
    @api.onchange('duration', 'car')
    def _onchange_duration_car(self):
        if self.duration and self.car:
            self.price = self.car.price_per_day
            self.total = self.duration * self.price
    
    @api.depends('duration', 'price')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.duration * rec.price