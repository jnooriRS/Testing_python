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
# Code Roman numerials explanation
# https://pencilprogrammer.com/python-programs/convert-integer-to-roman-numerals/#:~:text=So%2C%20to%20convert%20an%20integer%20into%20its%20corresponding,equivalent%20of%2013%20roman%20numerals%20in%20descending%20order.
