from application import Application
import pytest

fixture = Application()

@pytest.fixture(scope="session")
def base_fixture():
    return fixture