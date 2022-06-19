import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixture("data_load")
class TestExample(BaseClass):

    def test_edit_profile(self, data_load):
        print(data_load[0])
        log = self.get_logger()
        log.info(data_load[0])
        print(data_load[1])



