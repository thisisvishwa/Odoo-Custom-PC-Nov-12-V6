```python
from odoo import http
from odoo.http import request
import json

class MainController(http.Controller):

    @http.route('/product_config', type='json', auth='user')
    def product_config(self, **kwargs):
        product_config = request.env['product.configuration'].search([])
        return json.dumps(product_config.read(), default=str)

    @http.route('/inventory_mgmt', type='json', auth='user')
    def inventory_mgmt(self, **kwargs):
        inventory_mgmt = request.env['inventory.management'].search([])
        return json.dumps(inventory_mgmt.read(), default=str)

    @http.route('/pricing_engine', type='json', auth='user')
    def pricing_engine(self, **kwargs):
        pricing_engine = request.env['pricing.engine'].search([])
        return json.dumps(pricing_engine.read(), default=str)

    @http.route('/advanced_features', type='json', auth='user')
    def advanced_features(self, **kwargs):
        advanced_features = request.env['advanced.features'].search([])
        return json.dumps(advanced_features.read(), default=str)
```