import app


def test_title():
    assert app.title().startswith("Data ")


def test_asserting():
    assert False
