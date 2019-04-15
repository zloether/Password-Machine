import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from password_machine import pm
import pytest



@pytest.fixture
def app():
    app = pm.app
    app.debug = True
    return app.test_client()



def test_index(app):
    res = app.get("/")
    assert res.status_code == 200
    assert b"Password Machine" in res.data



def test_random_password_get(app):
    res = app.get("/random-password")
    assert res.status_code == 200
    assert len(res.data) == 32



def test_random_password_get_25(app):
    data = dict(length=25)
    res = app.get("/random-password", query_string=data)
    assert res.status_code == 200
    assert len(res.data) == 25



def test_random_password_post(app):
    data = dict(length=32, upper='true', lower='true', numbers='true', special='true')
    res = app.post("/random-password", data=data)
    assert res.status_code == 200
    assert len(res.data) == 32



def test_random_password_post_25(app):
    data = dict(length=25, upper='true', lower='true', numbers='true', special='true')
    res = app.post("/random-password", data=data)
    assert res.status_code == 200
    assert len(res.data) == 25