# Copyright
# License AGPL-3.0
import logging

from odoo import SUPERUSER_ID
from odoo.api import Environment
from odoo.tools.sql import column_exists, create_column

_logger = logging.getLogger(__name__)

COLUMNS = (
    ("sale_order", "price_total_no_discount"),
    ("sale_order", "discount_total"),
    ("sale_order_line", "price_total_no_discount"),
    ("sale_order_line", "discount_total"),
)


def pre_init_hook(cr):
    for table, column in COLUMNS:
        if not column_exists(cr, table, column):
            _logger.info("Create discount column %s in database", column)
            create_column(cr, table, column, "numeric")


def post_init_hook(cr, registry):
    _logger.info("Compute discount columns")
    env = Environment(cr, SUPERUSER_ID, {})

    query = """
    update sale_order_line
    set price_total_no_discount = price_total
    where discount = 0.0
    """
    cr.execute(query)

    query = """
        update sale_order
        set price_total_no_discount = amount_total
        """
    cr.execute(query)

    query = """
    select distinct order_id from sale_order_line where discount > 0.0;
    """

    cr.execute(query)
    order_ids = cr.fetchall()

    orders = env["sale.order"].search([("id", "in", order_ids)])
    orders.mapped("order_line")._update_discount_display_fields()
########
# product_variant_sale_price
def set_sale_price_on_variant(cr, registry, template_id=None):
    sql = """
        UPDATE product_product pp
        SET fix_price = pt.list_price + (
            SELECT COALESCE(SUM(ptav.price_extra), 0)
            FROM product_variant_combination pvc
            LEFT JOIN product_template_attribute_value ptav ON
                ptav.id = pvc.product_template_attribute_value_id
            WHERE pvc.product_product_id = pp.id
            AND ptav.product_tmpl_id = pt.id
        )
        FROM product_template pt
        WHERE pt.id = pp.product_tmpl_id
    """
    if template_id:
        sql += "AND pt.id = %s"
        cr.execute(sql, (template_id,))
    else:
        cr.execute(sql)