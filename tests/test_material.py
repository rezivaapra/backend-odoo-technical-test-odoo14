from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterialModule(TransactionCase):

    def setUp(self):
        super(TestMaterialModule, self).setUp()
        self.supplier = self.env['material.supplier'].create({'name': 'Test Supplier'})
        self.material_data = {
            'material_code': 'M001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id
        }

    def test_material_creation(self):
        material = self.env['material.material'].create(self.material_data)
        self.assertEqual(material.material_code, 'M001')

    def test_material_buy_price_validation(self):
        self.material_data['material_buy_price'] = 50
        with self.assertRaises(ValidationError):
            self.env['material.material'].create(self.material_data)

    def test_material_update(self):
        material = self.env['material.material'].create(self.material_data)
        material.write({'material_name': 'Updated Material'})
        self.assertEqual(material.material_name, 'Updated Material')

    def test_material_deletion(self):
        material = self.env['material.material'].create(self.material_data)
        material_id = material.id
        material.unlink()
        self.assertFalse(self.env['material.material'].browse(material_id).exists())
