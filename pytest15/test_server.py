# mark 标记

import pytest

@pytest.mark.androidtest
def test_send_http():
    pass

def test_sonething_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        pass

    def test_methods(self):
        pass

if __name__ == "__main__":
    pytest.main(["-v", "test_server.py::TestClass::test_method", "test_server,py::test_send_http"])
