from odoo import http
from odoo.http import request
import json

class MaterialController(http.Controller):
    @http.route(['/materials', '/materials/<string:material_type>'], methods=['GET'], csrf=True)
    def get_material(self, material_type=None, **kwargs):
        value = []
        if not material_type:
            materials = request.env['material.material'].search([])
            for material in materials:
                value.append({
                    'id': material.id,
                    'material_code': material.material_code,
                    'material_name': material.material_name,
                    'material_type': material.material_type,
                    'material_buy_price': material.material_buy_price,
                    'supplier_id.name': material.supplier_id.name
                })
            return json.dumps(value, indent=4)
        else:
            materials = request.env['material.material'].search([('material_type', '=', material_type)])
            for material in materials:
                value.append({
                    'id': material.id,
                    'material_code': material.material_code,
                    'material_name': material.material_name,
                    'material_type': material.material_type,
                    'material_buy_price': material.material_buy_price,
                    'supplier_id.name': material.supplier_id.name
                })
            return json.dumps(value, indent=4)
    
    @http.route('/materials/create', auth='public', type='json', methods=['POST'])
    def create_material(self, **kwargs):
        data = request.jsonrequest
        if not data:
            return {'succeed': False, 'message': 'Request body is empty. Please provide the necessary data.'}
        if data.get('material_buy_price') < 100:
            return {'succeed': False, 'message': 'Material Buy Price must be greater than or equal to 100.'}
        required_fields = ['material_code', 'material_name', 'material_type', 'material_buy_price', 'supplier_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return {'succeed': False, 'message': f'Missing required fields: {", ".join(missing_fields)}'}
        vals = {
            'material_code': data.get('material_code'),
            'material_name': data.get('material_name'),
            'material_type': data.get('material_type'),
            'material_buy_price': data.get('material_buy_price'),
            'supplier_id': data.get('supplier_id')
        }
        material = request.env['material.material'].sudo().create(vals)
        args = {'succeed': True, "ID" : material.id}
        return args

    @http.route('/materials/edit/<int:id>', auth='public', type='json', methods=['PUT'])
    def edit_material(self, id, **kwargs):
        data = request.jsonrequest
        material = request.env['material.material'].sudo().search([('id', '=', id)])
        if not material:
            return {'succeed': False,'message': 'Material not found.'}
        if not data:
            return {'succeed': False, 'message': 'Request body is empty. Please provide the necessary data.'}
        if data.get('material_buy_price') < 100:
            return {'succeed': False, 'message': 'Material Buy Price must be greater than or equal to 100.'}
        required_fields = ['material_code', 'material_name', 'material_type', 'material_buy_price', 'supplier_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return {'succeed': False, 'message': f'Missing required fields: {", ".join(missing_fields)}'}
        vals = {
            'material_code': data.get('material_code'),
            'material_name': data.get('material_name'),
            'material_type': data.get('material_type'),
            'material_buy_price': data.get('material_buy_price'),
            'supplier_id': data.get('supplier_id')
        }
        material.sudo().write(vals)
        args = {'succeed': True}
        return args
        
    @http.route('/materials/delete/<int:id>', auth='public', methods=['DELETE'], csrf=True)
    def delete_material(self, id, **kwargs):
        material = request.env['material.material'].sudo().search([('id', '=', id)])
        if material:
            material.sudo().unlink()
            return json.dumps({'status': 'success', 'message': 'Material deleted successfully.'}, indent=4)
        else:
            return json.dumps({'status': 'error', 'message': 'Material not found.'}, indent=4)
        
    