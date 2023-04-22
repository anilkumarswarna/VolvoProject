import pytest
import time
from Demo.Demo.utils import settingsLib



@pytest.fixture
def obj():
    return settingsLib.settings()

@pytest.fixture
def launch_settings(obj):
    obj.LaunchSettings()
    time.sleep(2)
    yield
    obj.backKey()
    obj.backKey()
    obj.backKey()
    obj.backKey()

