from app.reports.models import Daily
from unchained.fixtures import load_db


def daily(test):
    def test_generate(self):
        load_db(Daily)
        test(self)
    return test_generate
