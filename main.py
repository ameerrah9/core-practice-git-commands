import pytest


def always_returns_true():
    print("why is this not working?")


def test_always_returns_true():
    assert always_returns_true()
