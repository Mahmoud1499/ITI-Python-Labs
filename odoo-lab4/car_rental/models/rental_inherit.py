from odoo import models, fields, api


class CarRentalCarInherit(models.Model):
    _inherit = 'car.rental.cars'   

    date = fields.Date(string='Date', required=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)
    duration = fields.Float(string='Duration (days)', compute='_compute_duration', store=True)

    @api.depends('price', 'date')
    def _compute_total(self):
        for record in self:
            record.total = record.price * record.duration

    @api.depends('date')
    def _compute_duration(self):
        for record in self:
            if record.date:
                start_date = fields.Date.from_string(record.date)
                end_date = fields.Date.today()
                delta = end_date - start_date
                record.duration = delta.days