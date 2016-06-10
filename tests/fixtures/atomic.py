from app.atomic.models import Store, Order, OrderItem, Customer, Product
from unchained.fixtures import load_db


def store(test):
    def test_generate(self):
        load_db(Store)
        test(self)
    return test_generate


def product(test):
    def test_generate(self):
        load_db(Product)
        test(self)
    return test_generate


def order(test):
    def test_generate(self):
        load_db(Order)
        load_db(OrderItem)
        test(self)
    return test_generate


def customer(test):
    def test_generate(self):
        load_db(Customer)
        test(self)
    return test_generate

