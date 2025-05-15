{
    "name": "App Launcher Demo",
    "version": "16.0.1.0",
    "summary": "Modulo dimostrativo: banner HTML nella schermata iniziale di Odoo",
    "category": "Interface",
    "author": "Ruocco Pietro Paolo",
    "website": "https://cactus.farm",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": [
        "views/app_drawer_inherit.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'applauncher_demo/static/src/js/dynamic_banner.js',
        ],
    },
    "installable": True,
    "application": False,
}