```python
from odoo.tests import common

class TestInventoryManagement(common.TransactionCase):

    def setUp(self):
        super(TestInventoryManagement, self).setUp()
        self.Inventory = self.env['inventory.management']

    def test_stock_level_tracking(self):
        # Create a new inventory record
        inventory = self.Inventory.create({
            'name': 'Test Inventory',
            'stock_level': 100,
        })

        # Simulate a sale
        inventory.adjust_stock(-10)
        self.assertEqual(inventory.stock_level, 90, "Stock level not adjusted correctly after sale")

        # Simulate a return
        inventory.adjust_stock(5)
        self.assertEqual(inventory.stock_level, 95, "Stock level not adjusted correctly after return")

        # Simulate a cancellation
        inventory.adjust_stock(5)
        self.assertEqual(inventory.stock_level, 100, "Stock level not adjusted correctly after cancellation")

    def test_alerts_and_notifications(self):
        # Create a new inventory record
        inventory = self.Inventory.create({
            'name': 'Test Inventory',
            'stock_level': 100,
            'low_stock_threshold': 50,
        })

        # Simulate sales to bring stock level below threshold
        inventory.adjust_stock(-60)
        self.assertTrue(inventory.low_stock_alert, "Low stock alert not triggered when stock level is below threshold")

        # Simulate restocking to bring stock level above threshold
        inventory.adjust_stock(60)
        self.assertFalse(inventory.low_stock_alert, "Low stock alert not cleared when stock level is above threshold")
```