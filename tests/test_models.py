import unittest
from pydantic import ValidationError
from broken_shop.models import Customer, Address, Product, Order


class CustomerContractTests(unittest.TestCase):
    def test_nickname_may_be_omitted(self):
        self.assertIsNone(Customer(name='Synthetic Ada', phone=None).nickname)

    def test_phone_may_be_omitted(self):
        self.assertIsNone(Customer(name='Synthetic Ada', nickname=None).phone)

    def test_apartment_may_be_omitted(self):
        self.assertIsNone(Address(street='123 Example Street', instructions=None).apartment)

    def test_instructions_may_be_omitted(self):
        self.assertIsNone(Address(street='123 Example Street', apartment=None).instructions)

    def test_description_may_be_omitted(self):
        self.assertIsNone(Product(sku='FAKE-1', category=None).description)

    def test_category_may_be_omitted(self):
        self.assertIsNone(Product(sku='FAKE-1', description=None).category)

    def test_coupon_may_be_omitted(self):
        self.assertIsNone(Order(order_id='FAKE-ORDER', notes=None).coupon)

    def test_notes_may_be_omitted(self):
        self.assertIsNone(Order(order_id='FAKE-ORDER', coupon=None).notes)

    def test_explicit_null_is_valid(self):
        self.assertIsNone(Customer(name='Synthetic Ada', nickname=None, phone=None).nickname)

    def test_object_nickname_stays_invalid(self):
        with self.assertRaises(ValidationError):
            Customer(name='Synthetic Ada', nickname={'bad': 'value'}, phone=None)
