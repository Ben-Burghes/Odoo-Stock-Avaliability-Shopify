from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    shopify_product = fields.Boolean("Shopify Product", default=False)
