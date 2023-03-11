import pytest

import data


def test_generate_data():
    assert data.generate_data()[0]["x"] == 0

def test_exception():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        raise ValueError("ABC 123 XYZ")
