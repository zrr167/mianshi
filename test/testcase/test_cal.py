import pytest

from baw.calculate import Calculate
from caw import Filereader, assert_until


@pytest.fixture(scope='session')
def ready_test():
    print("测试开始")
    yield
    print("测试结束")


@pytest.fixture()
def ready_case():
    print("计算开始")
    yield
    print("计算结束")


@pytest.fixture(params=Filereader.read_yaml("case0.yaml"))
def rucan0(request):
    return request.param


@pytest.fixture(params=Filereader.read_yaml("case1.yaml"))
def rucan1(request):
    return request.param


@pytest.mark.P0
def test_cal0(rucan0, ready_test, ready_case):
    ac = Calculate().cal(**rucan0["data"])
    print(ac)
    assert_until.assert_res(ac, rucan0['expect'], ("result",))


@pytest.mark.P1
def test_cal1(rucan1, ready_test, ready_case):
    ac = Calculate().cal(**rucan1["data"])
    print(ac)
    assert_until.assert_res(ac, rucan1['expect'], ("result",))
