 
{
    'name': 'Delight POS theme | Advance POS Theme | point of sale theme | Theme POS | Odoo POS theme',
    'category': 'Website',
    'version': '17.0.1.0.0',
    'author': 'Terabits Technolab',
    'website': 'https://www.terabits.xyz', 
    'images': [
        'static/description/banner.gif'
    ],
    'description': """ Delight POS theme | Advanced POS theme | Theme POS | Odoo POS theme | Shopon POS | Multipurpose odoo pos theme | point of sale theme | ShopOn POS |
        POS restaurant theme | POS theme | all in one pos | pos layout |pos order| pos cash in cashout| pos order| pos visibility control| product suggestion|Odoo POS customization |New customized pos theme for the modern generation |
        POS Brand New User Interface| Redesigned Look for POS | New Look and Features to existing POS Design| Gen X | Design |Custom POS theme |Retail POS system |POS customization | POS theme in Odoo | POS Dashboard | POS Mobile interface | POS tablet interface |
        POS Theme for Odoo | Mobile POS Theme for Odoo | Responsive Point of Sale Theme |Touchscreen POS Theme for Odoo | Modern POS Theme for | POS User friendly ui|
        Easy to Use POS Theme for Odoo | Optimized POS Theme for Odoo | Lightweight POS Theme for Odoo | Professional POS Theme for Odoo|Multi-Device POS Theme |Responsive POS Theme with Color Flexibility|Flexible POS Theme for All Devices |Colorful POS Theme for Any Device|Mobile-Friendly POS Theme |Touchscreen POS Theme with Custom Colors
        Modern POS Theme with Unlimited Color Options | Professional POS Theme for Any Device|Easy to Use POS Theme with Color Customization | Retail Point Of Sale |
        Retail POS System | Retail Point Of Sale System | POS table orders merge | POS merge tables | Order list merge | POS order management | POS table management
        """,
    'summary': """ 
        Delight POS theme | Advanced POS theme | Theme POS | Odoo POS theme | Shopon POS | Multipurpose odoo pos theme | point of sale theme | ShopOn POS |
        POS restaurant theme | POS theme | all in one pos | pos layout |pos order| pos visibility control| product suggestion|Odoo POS customization |New customized pos theme for the modern generation |
        POS Brand New User Interface| Redesigned Look for POS | New Look and Features to existing POS Design| Gen X | Design |Custom POS theme |Retail POS system |POS customization | POS theme in Odoo | POS Dashboard | POS Mobile interface | POS tablet interface 
        
        Our odoo Point of Sale split bill module allows the user to split orders by persons. You can split the order and get reciespt of the splited amount.
        POS split bill | split by person | split order | split invoice | pos split invoice | devide amount in group | split by group 
        Point of sale split bill | split bill on point of sale | pos restaurant split table | pos split restaurant table 
        Odoo POS Split Bill | Point of Sale Split Order |Invoice Splitting in Odoo | Split Payment POS Module | POS Order Split by Persons|
        
        Simplify Access Management | Manage - Hide Menu, Submenu, Fields, Action, Reports, Views, | Restrict/Read-Only User, Apps,  Fields, Export, Archive, Actions, Views, Reports, Delete items | Manage Access rights from one place | Hide Tabs and buttons | Multi Company supported. | Access Manager
        Bill Splitting and Invoicing | Splitting Orders by Customers |POS Multi-Invoice Generation | Odoo POS Split Amounts | Separate Invoicing for Split Orders.
        Display POS Stock Quantity on POS screen stock Product stock in POS product stock Quantity POS Order stock POS Mobile POS Inventory management pos stocks pos item stock point of sale stock POS Product Warehouse Quantity pos product qty pos product Quantity
    """,
    'depends': [
        'point_of_sale', 
    ], 
    'assets': {  
        'point_of_sale.assets': [  
            # bootsrap assets
            ('include', 'web._assets_bootstrap'), 
            #---------
            '/delight_pos_theme_bits/static/src/scss/pos.scss', 
            '/delight_pos_theme_bits/static/src/scss/sidebar.scss',
            '/delight_pos_theme_bits/static/src/scss/ticket_screen.scss',
            '/delight_pos_theme_bits/static/src/scss/product_screen.scss',
            '/delight_pos_theme_bits/static/src/scss/_tables.scss', 
            '/delight_pos_theme_bits/static/src/scss/profile_view.scss',
            '/delight_pos_theme_bits/static/src/scss/model_dialog.scss',
            '/delight_pos_theme_bits/static/src/scss/numpad.scss',
            '/delight_pos_theme_bits/static/src/scss/payment_screen.scss',
            '/delight_pos_theme_bits/static/src/scss/partner_list_screen.scss',
            '/delight_pos_theme_bits/static/src/xml/Screens/pos_bits.xml',
            '/delight_pos_theme_bits/static/src/js/screens/ProductScreen.js', 
            '/delight_pos_theme_bits/static/src/xml/Screens/ProductScreen.xml',
            '/delight_pos_theme_bits/static/src/js/screens/TicketScreen.js',
            '/delight_pos_theme_bits/static/src/xml/Screens/TicketScreen.xml', 
            '/delight_pos_theme_bits/static/src/js/Chrome.js',
            '/delight_pos_theme_bits/static/src/js/PosContentHeader.js',   
            '/delight_pos_theme_bits/static/src/js/ChromeAdapter.js',
            '/delight_pos_theme_bits/static/src/xml/Screens/PartnerListScreen.xml', 
            '/delight_pos_theme_bits/static/src/xml/Chrom.xml',
            '/delight_pos_theme_bits/static/src/xml/Screens/PartnerDetailsEdit.xml',
            '/delight_pos_theme_bits/static/src/xml/PosContentHeader.xml', 
            '/delight_pos_theme_bits/static/src/xml/Screens/StatusButtons.xml',  
            '/delight_pos_theme_bits/static/src/js/mobile_view/**/*',
            '/delight_pos_theme_bits/static/src/xml/mobile_view/**/*'
        ],
    },

    'data': [ 
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/point_of_sale_index.xml',
        'views/res_config_settings.xml', 
        'views/pos_theme_config_view.xml',
        'views/pos_config_view.xml'
    ], 
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
    'price': 199.99,
    'currency': 'USD',
    'live_test_url': 'https://www.terabits.xyz/request_demo?source=index&version=16&app=delight_pos_theme_bits',
}
