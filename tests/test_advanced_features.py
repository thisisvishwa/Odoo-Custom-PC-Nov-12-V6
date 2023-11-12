```python
from odoo.tests import common

class TestAdvancedFeatures(common.TransactionCase):

    def setUp(self):
        super(TestAdvancedFeatures, self).setUp()
        self.AdvancedFeatures = self.env['advanced.features']

    def test_3d_visualization(self):
        # Create a new advanced feature with 3D visualization
        advanced_feature = self.AdvancedFeatures.create({
            'name': '3D Visualization',
            'description': '3D visualization of PC components',
        })

        # Check if the advanced feature is created
        self.assertEqual(advanced_feature.name, '3D Visualization')

        # Test the 3D visualization method
        result = advanced_feature.visualize_3d()
        self.assertTrue(result, '3D Visualization failed')

    def test_performance_estimation(self):
        # Create a new advanced feature with performance estimation
        advanced_feature = self.AdvancedFeatures.create({
            'name': 'Performance Estimation',
            'description': 'Estimate the performance of the selected PC components',
        })

        # Check if the advanced feature is created
        self.assertEqual(advanced_feature.name, 'Performance Estimation')

        # Test the performance estimation method
        result = advanced_feature.estimate_performance()
        self.assertTrue(result, 'Performance Estimation failed')

    def test_modularity(self):
        # Create a new advanced feature
        advanced_feature = self.AdvancedFeatures.create({
            'name': 'Modular Feature',
            'description': 'Test feature for modularity',
        })

        # Check if the advanced feature is created
        self.assertEqual(advanced_feature.name, 'Modular Feature')

        # Test the toggle method
        advanced_feature.toggle_feature()
        self.assertFalse(advanced_feature.active, 'Feature toggle failed')
```
