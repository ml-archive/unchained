from flask import Blueprint, render_template
from app import db
from app.reports.models import Daily
import datetime


reports = Blueprint('reports', __name__, url_prefix='/reports')


@reports.route('/', methods=['GET', ])
def index():
    return render_template("reports/index.html", now=datetime.datetime.now())
