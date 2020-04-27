from odoo import api, models, tools


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    @tools.ormcache("self.ids", "self.env.uid",
                    "self.env.user.current_session")
    def wishlisted(self):
        """Check if all products are wishlisted in current session."""
        wishes = set(self.env["website"].get_current_website()
                     .wishlisted_product_template_ids())
        return set(self.ids) <= wishes
