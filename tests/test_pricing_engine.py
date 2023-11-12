```python
from odoo.tests import common

class TestPricingEngine(common.TransactionCase):

    def setUp(self):
        super(TestPricingEngine, self).setUp()
        self.PricingEngine = self.env['pricing.engine']

    def test_price_calculation(self):
        # Create a test pricing engine
        pricing_engine = self.PricingEngine.create({
            'name': 'Test Pricing Engine',
            'base_cost': 1000.0,
            'current_promotion': 10.0,
        })

        # Test price calculation
        self.assertEqual(pricing_engine.calculate_price(), 900.0, "Price calculation failed")

    def test_promotional_adjustments(self):
        # Create a test pricing engine
        pricing_engine = self.PricingEngine.create({
            'name': 'Test Pricing Engine',
            'base_cost': 1000.0,
            'current_promotion': 10.0,
        })

        # Test promotional adjustments
        pricing_engine.apply_promotion(20.0)
        self.assertEqual(pricing_engine.calculate_price(), 800.0, "Promotional adjustment failed")

    def test_scalability(self):
        # Create a large number of pricing engines
        for i in range(10000):
            self.PricingEngine.create({
                'name': 'Test Pricing Engine ' + str(i),
                'base_cost': 1000.0,
                'current_promotion': 10.0,
            })

        # Test scalability by calculating price for all pricing engines
        for pricing_engine in self.PricingEngine.search([]):
            pricing_engine.calculate_price()
```
