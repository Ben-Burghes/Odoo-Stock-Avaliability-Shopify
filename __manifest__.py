{
    "version": "15.0.2.3.0",
    "name": "wwuk_shopify_stock_availability",
    "summary": "Calculate stock availability for BOMs, Kits, etc.",
    "category": "Warehouse",
    "application": False,
    "author": "Glo Networks",
    "website": "https://www.tcgroupuk.com/",
    "license": "Other proprietary",
    "depends": [
        "wwuk_stock_availability",
        "wwuk_product",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [],
    "assets": {},
    "post_init_hook": "post_init_hook",
    "installable": True,
}
