from odoo import api, models


class StockAvailability(models.Model):
    _inherit = "stock.availability"

    @api.model
    def _dirty(self, product_id, location_id=None, warehouse_id=None):
        """
        Mark a product_id at warehouse location as dirty.
        """

        if location_id:
            warehouse_id = location_id.warehouse_id

        if not warehouse_id:
            return

        # Call super to handle the default dirty marking logic
        res = super()._dirty(product_id, location_id, warehouse_id)

        if isinstance(product_id, int):
            product_id = self.env["product.product"].browse(product_id)

        # TODO: This parent determination can be relatively
        # expensive. Should this really be upfront in the time sensitive areas where
        # _dirty is called? Probably not.

        # Determine all related parent products to also mark as dirty
        related_products = self._determine_parents_for(product_id)

        if not related_products or not warehouse_id:
            return res

        with self.pool.cursor() as cr:
            # Using a new cursor to avoid long on-going queries, such as price list
            # changes, cache calculations, etc.
            cr.execute(
                """
                INSERT INTO stock_availability_dirty_shopify (product_id, warehouse_id)
                SELECT x.product_id, x.warehouse_id
                FROM unnest(%s, %s) AS x(product_id, warehouse_id)
                ON CONFLICT (product_id, warehouse_id) DO NOTHING;
                """,
                [related_products.ids, [warehouse_id.id] * len(related_products.ids)],
            )

        return res

    @api.autovacuum
    def _gc_invalid_shopify_records(self):
        # Clean any potentially mangled records because we're not using FKs due to using
        # new cursors to avoid locking problems
        cr = self.env.cr

        cr.execute(
            """
            DELETE FROM stock_availability_dirty_shopify WHERE NOT EXISTS (
                SELECT
                    1
                FROM product_product
                WHERE
                    id = stock_availability_dirty_shopify.product_id
            )
            """
        )
