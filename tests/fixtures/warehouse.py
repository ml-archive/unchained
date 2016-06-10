from app.warehouse.stage.models import StageEmporio
from unchained.fixtures import load_db


def emporio(test):
    def test_generate(self):
        load_db(StageEmporio)
        test(self)
    return test_generate

