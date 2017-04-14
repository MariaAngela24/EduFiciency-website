
from server import app
import unittest
from model import db, connect_to_db

class FlaskTests(unittest.TestCase):


    def setUp(self):
        """Set up by creating fake client."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'


    def test_index(self):
        """Test for homepage."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("<h1>Welcome to EduFiciency</h1>", result.data)


    def test_romeo_page(self):
        """Test for Romeo product page."""

        result = self.client.get("/products")
        self.assertEqual(result.status_code, 200)
        self.assertIn("O Romeo, Romeo", result.data)


    def test_about_us_page(self):
        """Test for about us page."""

        result = self.client.get("/about_us")
        self.assertEqual(result.status_code, 200)
        self.assertIn("Maria Mendiburo", result.data)


    def test_contact_form(self):
        """Test for contact form."""

        result = self.client.get("/contact")
        self.assertEqual(result.status_code, 200)
        self.assertIn("We'd love to hear from you!", result.data)


if __name__ == '__main__':
    unittest.main()