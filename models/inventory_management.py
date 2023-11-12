```python
from odoo import models, fields, api

class InventoryManagement(models.Model):
    _name = 'inventory.management'
    _description = 'Inventory Management'

    product_id = fields.Many2one('product.configuration', string='Product')
    stock_level = fields.Integer(string='Stock Level', compute='_compute_stock_level')
    low_stock_alert = fields.Boolean(string='Low Stock Alert', compute='_compute_low_stock_alert')

    @api.depends('product_id')
    def _compute_stock_level(self):
        for record in self:
            # Implement logic to calculate stock level based on sales, returns, and cancellations
            record.stock_level = 0

    @api.depends('stock_level')
    def _compute_low_stock_alert(self):
        for record in self:
            # Implement logic to set low_stock_alert True if stock level is below a certain threshold
            record.low_stock_alert = False

    @api.model
    def create(self, vals):
        record = super().create(vals)
        # Implement logic to adjust stock level after a new inventory record is created
        return record

    def write(self, vals):
        result = super().write(vals)
        # Implement logic to adjust stock level after an inventory record is updated
        return result

    def unlink(self):
        # Implement logic to adjust stock level before an inventory record is deleted
        result = super().unlink()
        return result
```