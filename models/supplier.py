from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.supplier'
    _description = 'Supplier for Sale'

    name = fields.Char(string='Nama Supplier', required=True)