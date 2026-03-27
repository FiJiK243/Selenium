import pytest


def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed(xfail=False):
    assert False == xfail


@pytest.mark.skip
def test_skipped(skip=False):
    assert False == skip


test_succeed()
test_not_succeed()
test_skipped()
