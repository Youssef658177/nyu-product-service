import unittest
from service import app
from service.models import Product, db, Category
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    """Test cases for Product Model"""

    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        db.create_all()

    def setUp(self):
        db.session.query(Product).delete()
        db.session.commit()

    # 1. Test Read
    def test_read_a_product(self):
        product = ProductFactory()
        product.create()
        found_product = Product.find(product.id)
        self.assertEqual(found_product.id, product.id)
        self.assertEqual(found_product.name, product.name)

    # 2. Test Update
    def test_update_a_product(self):
        product = ProductFactory()
        product.create()
        product.name = "Updated Name"
        product.update()
        self.assertEqual(Product.find(product.id).name, "Updated Name")

    # 3. Test Delete
    def test_delete_a_product(self):
        product = ProductFactory()
        product.create()
        self.assertEqual(len(Product.all()), 1)
        product.delete()
        self.assertEqual(len(Product.all()), 0)

    # 4. Test List All
    def test_list_all_products(self):
        products = ProductFactory.create_batch(5)
        for p in products:
            p.create()
        self.assertEqual(len(Product.all()), 5)

    # 5. Test Find by Name
    def test_find_by_name(self):
        products = ProductFactory.create_batch(3)
        for p in products:
            p.create()
        name = products[0].name
        count = len([p for p in products if p.name == name])
        found = Product.find_by_name(name)
        self.assertEqual(found.count(), count)

    # 6. Test Find by Category
    def test_find_by_category(self):
        products = ProductFactory.create_batch(3)
        for p in products:
            p.create()
        category = products[0].category
        count = len([p for p in products if p.category == category])
        found = Product.find_by_category(category)
        self.assertEqual(found.count(), count)

    # 7. Test Find by Availability
    def test_find_by_availability(self):
        products = ProductFactory.create_batch(3)
        for p in products:
            p.create()
        available = products[0].available
        count = len([p for p in products if p.available == available])
        found = Product.find_by_availability(available)
        self.assertEqual(found.count(), count)
