import unittest
from service import app
from service.models import db, Product
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):
    """Test cases for Product Web Service"""

    def setUp(self):
        self.client = app.test_client()
        db.session.query(Product).delete()
        db.session.commit()

    def test_get_product(self):
        product = ProductFactory()
        product.create()
        resp = self.client.get(f"/products/{product.id}")
        self.assertEqual(resp.status_code, 200)

    def test_update_product(self):
        product = ProductFactory()
        product.create()
        new_data = {"name": "New Laptop", "price": 999.0, "available": True, "category": "ELECTRONICS", "description": "None"}
        resp = self.client.put(f"/products/{product.id}", json=new_data)
        self.assertEqual(resp.status_code, 200)

    def test_delete_product(self):
        product = ProductFactory()
        product.create()
        resp = self.client.delete(f"/products/{product.id}")
        self.assertEqual(resp.status_code, 204)

    def test_get_product_list(self):
        resp = self.client.get("/products")
        self.assertEqual(resp.status_code, 200)

    def test_query_by_name(self):
        product = ProductFactory()
        product.create()
        resp = self.client.get(f"/products?name={product.name}")
        self.assertEqual(resp.status_code, 200)

    def test_query_by_category(self):
        product = ProductFactory()
        product.create()
        resp = self.client.get(f"/products?category={product.category.name}")
        self.assertEqual(resp.status_code, 200)

    def test_query_by_availability(self):
        product = ProductFactory()
        product.create()
        resp = self.client.get(f"/products?available={str(product.available).lower()}")
        self.assertEqual(resp.status_code, 200)
