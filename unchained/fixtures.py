from app import db
import dateutil.parser
import json
import glob
import re

ISO_DATE = '[\d]{4}-[\d]{2}-[\d]{2}'


'''
Really just a sort of (reasonable) experiment to mix the json-fixtures-like concept from
Django with the decorator-concept from py.test since Flask doesn't quite have a solution for
managing fixtures. It is really in a couple pieces right now to evaluate the concept.

You then define decorators as follows:

def product(test):
    def test_generate(self):
        load_db(Product)
        test(self)
    return test_generate

Unfortunately this gets tedious / redundant so we need to come up way to make these dynamically.
Ideally you just define the fixture and bada bing bada boom, fixtures get picked up and go.
'''


def _module_and_class_name(cls):
    return '{0}.{1}'.format(cls.__module__, cls.__name__)


def _convert_to_date(fields):  # kind of annoying but conversion isn't quite automatic in sqlite
    pattern = re.compile(ISO_DATE)
    for field in fields:
        if isinstance(fields[field], str) and pattern.search(fields[field]):
            fields[field] = dateutil.parser.parse(fields[field])
    return fields


def _all_fixtures():
    fixtures = {}
    for file in glob.glob("./tests/fixtures/*.json"):
        with open(file) as data_file:
            fixtures.update(json.load(data_file))
    return fixtures


def load_db(cls):
    for fields in _all_fixtures()[_module_and_class_name(cls)]:
        db.session.add(cls(**_convert_to_date(fields)))
    db.session.commit()
