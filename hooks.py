from openupgradelib import openupgrade

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    # Create the Shopify stock synchronization table with the new name
    if not openupgrade.table_exists(env.cr, "stock_availability_dirty_shopify"):
        openupgrade.logged_query(
            env.cr,
            """
            CREATE TABLE stock_availability_dirty_shopify (
                product_id integer NOT NULL,

                warehouse_id integer NOT NULL,

                date_added timestamp with time zone NOT NULL DEFAULT now(),

                CONSTRAINT stock_availability_dirty_shopify_product_id_warehouse_id_uniq
                UNIQUE (product_id, warehouse_id)
            )
            """,
        )
