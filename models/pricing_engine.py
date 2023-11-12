```python
from odoo import models, fields, api

class PricingEngine(models.Model):
    _name = 'pricing.engine'
    _description = 'Pricing Engine'

    base_cost = fields.Float(string='Base Cost')
    current_promotions = fields.Many2many('promotion', string='Current Promotions')
    custom_configurations = fields.Many2many('product.configuration', string='Custom Configurations')

    @api.depends('base_cost', 'current_promotions', 'custom_configurations')
    def compute_price(self):
        for record in self:
            price = record.base_cost
            for promotion in record.current_promotions:
                price -= promotion.discount
            for configuration in record.custom_configurations:
                price += configuration.price
            record.price = price

    price = fields.Float(string='Price', compute='compute_price')

    def apply_promotion(self, promotion):
        self.ensure_one()
        self.current_promotions = [(4, promotion.id)]

    def remove_promotion(self, promotion):
        self.ensure_one()
        self.current_promotions = [(3, promotion.id)]
```