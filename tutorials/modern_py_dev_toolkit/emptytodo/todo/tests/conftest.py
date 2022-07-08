import pytest
from flask import Flask
from todo import db as _db

@pytest.fixture
def test_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    # The following line is needed to suppress SQLALCHEMY_TRACK_MODIFICATIONS warning
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    
    _db.init_app(app)

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()
