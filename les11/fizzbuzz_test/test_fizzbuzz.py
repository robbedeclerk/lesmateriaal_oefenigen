import pytest


def test_call_fizzbuzz():
    fizzbuzz(0)

#def test_fizzbuzz_with_0():
#    assert fizzbuzz()=="fizzbuzz"

def test_fizzbuzz_with_1():
    assert fizzbuzz(1)==1

def test_fizzbuzz_with_3():
    assert fizzbuzz(3)=="fizz"

def test_fizzbuzz_with_5():
    assert fizzbuzz(5)=="buzz"

def test_fizzbuzz_with_6():
    assert fizzbuzz(6)=="fizz"

def test_fizzbuzz_with_10():
    assert fizzbuzz(10)=="buzz"

def test_fizzbuzz_with_15():
    assert fizzbuzz(15)=="fizzbuzz"

def test_fizzbuzz_with_minus_1():
    assert fizzbuzz(-1)==-1

def test_fizzbuzz_with_minus_3():
    assert fizzbuzz(-3)=='fizz'

def is_multiple(number,base):
    return number%base==0

def fizzbuzz(getal):
    if is_multiple(getal,base:3) and if is_multiple(getal,base:5):
        return 'fizzbuzz'
    if is_multiple(getal,base:3):
        return 'fizz'
    elif is_multiple(getal,base:5):
        return 'buzz'
    else:
        return getal