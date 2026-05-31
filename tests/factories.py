import factory
from factory.fuzzy import FuzzyChoice, FuzzyFloat
from service.models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(choices=["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard"])
    description = factory.Faker("text")
    price = FuzzyFloat(10.0, 1000.0)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(choices=[Category.ELECTRONICS, Category.CLOTHING, Category.HOME, Category.BOOKS])
