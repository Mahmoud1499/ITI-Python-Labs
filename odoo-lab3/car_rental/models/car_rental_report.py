from odoo import models, fields, api


class CarRentalReport(models.AbstractModel):
    _name = 'report.car_rental.report_car_rental_invoice'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['report']
        rental_obj = self.env['car.rental.sales']
        report = report_obj._get_report_from_name(
            'car_rental.report_car_rental_invoice')
        docs = rental_obj.browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'data': data,
        }
