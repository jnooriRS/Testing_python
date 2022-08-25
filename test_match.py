import pytest


def myfunc():
    raise ValueError("Exception 122 raised")


def test_match():
    with pytest.raises(ValueError, match="123"):
        myfunc()


# Using regex as a comparrison
# def test_match():
#     with pytest.raises(ValueError, match=r".* 123 .*"):
#         myfunc()
# should submit to main
