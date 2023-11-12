{
    'name': 'PC Component Configuration',
    'version': '16.0.1.0.0',
    'category': 'Productivity',
    'summary': 'PC Component Configuration, Inventory Management, Pricing Engine, and Advanced Features',
    'sequence': 10,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'product', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/product_categories.xml',
        'views/product_configuration_view.xml',
        'views/inventory_management_view.xml',
        'views/pricing_engine_view.xml',
        'views/advanced_features_view.xml',
        'controllers/main_controller.py',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
PC Component Configuration
==========================
This module provides functionalities for:
- Product Configuration: User-centric, intuitive interface for PC component selection with real-time compatibility checks and custom configurations.
- Inventory Management: Robust system for tracking and updating inventory levels in real-time.
- Pricing Engine: Dynamic pricing engine that adjusts prices based on selected components, promotions, and market factors.
- Advanced Features: Implementation of advanced features such as 3D visualization, performance estimation, and more.
    """,
    'license': 'LGPL-3',
}