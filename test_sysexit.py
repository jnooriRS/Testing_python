import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


# https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
# Various types of tests
