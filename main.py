import pytest


def always_returns_true():
<<<<<<< HEAD
    print("why is this not working?")
=======
    return True
>>>>>>> 0a1492aff2e73626ae3869012d11803c9218c2bd


def test_always_returns_true():
    assert always_returns_true()
