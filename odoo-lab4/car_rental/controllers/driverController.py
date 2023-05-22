from odoo import http
from odoo.http import request

class DriversController(http.Controller):
    
    @http.route('/drivers/list', auth='public', type='json', methods=['GET'])
    def list_drivers(self):
        Drivers = request.env['car.rental.drivers'].sudo().search([])
        driver_data = []
        
        for driver in Drivers:
            driver_data.append({
                'name': driver.name,
                'license_number': driver.license_number,
            })
        
        return {
            'success': True,
            'data': driver_data
        }
