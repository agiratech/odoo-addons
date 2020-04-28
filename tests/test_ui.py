from openerp.tests.common import HttpCase


class UICase(HttpCase):
    def test_ui_website(self):
        """Test frontend tour."""
        self.phantom_js(
            url_path="/",
            code="odoo.__DEBUG__.services['web.Tour']"
                 ".run('test_product_wishlist', 'test')",
            ready="odoo.__DEBUG__.services['web.Tour']"
                  ".tours.test_product_wishlist")
