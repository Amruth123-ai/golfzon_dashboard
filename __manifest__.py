{
    "name": "Golfzon Dashboard",
    "version": "1.0.0",
    "category": "Custom",
    "summary": "Professional Golfzon Dashboard with Enhanced UI and Location-based Weather",
    "description": """
    Enhanced Golfzon Dashboard featuring:
    - Professional sidebar navigation
    - Real-time KPI metrics
    - Interactive charts and analytics
    - Location-based hourly weather updates
    - Activity tracking
    - Quick actions panel
    - Responsive design
    - Improved reservation details layout
    """,
    "author": "Sri Hari",
    "depends": ["web", "base"],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/templates.xml",
        "data/dummy_data.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "golfzon_dashboard/static/src/scss/dashboard.scss",
            "golfzon_dashboard/static/lib/chartjs/Chart.min.js",
            "golfzon_dashboard/static/src/js/dashboard_client.js",
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css',
        ],
        "web.assets_frontend": [
            "golfzon_dashboard/static/src/scss/dashboard.scss",
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css',
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
