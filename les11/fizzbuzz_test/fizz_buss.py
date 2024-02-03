import pytest


def test_call_fizzbuzz():
    fizzbuzz(0)

#def test_fizzbuzz_with_0():
#    assert fizzbuzz()=="fizzbuzz"

def test_fizzbuzz_with_1():
    assert fizzbuzz(1)==1

def test_fizzbuzz_with_3():
    assert fizzbuzz(1)=="fizz"

def fizzbuzz(getal):
    if getal == 3:
        return 'fizz'