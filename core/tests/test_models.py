from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Brand, Supplier, Category, Product
from decimal import Decimal
from django.utils import timezone
import datetime


def make_valid_cedula():
    # construct a simple valid cedula for tests: 0912345675 (computed checksum)
    return '0912345675'


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.brand = Brand.objects.create(description='MarcaTest', user=self.user)
        self.category1 = Category.objects.create(description='CatA', user=self.user)
        self.category2 = Category.objects.create(description='CatB', user=self.user)
        self.supplier = Supplier.objects.create(
            name='Supp1', ruc=make_valid_cedula(), address='Addr', phone='0999999999', user=self.user
        )
        self.product = Product.objects.create(
            description='Prod1', price=Decimal('9.99'), stock=10,
            expiration_date=timezone.now() + datetime.timedelta(days=10),
            brand=self.brand, user=self.user, supplier=self.supplier
        )
        self.product.categories.add(self.category1, self.category2)

    def test_str_methods(self):
        self.assertEqual(str(self.brand), 'MarcaTest')
        self.assertEqual(str(self.supplier), 'Supp1')
        self.assertEqual(str(self.category1), 'CatA')
        self.assertEqual(str(self.product), 'Prod1')

    def test_get_categories_property(self):
        cats = self.product.get_categories
        # categories are ordered by description
        self.assertIn('CatA', cats)
        self.assertIn('CatB', cats)
