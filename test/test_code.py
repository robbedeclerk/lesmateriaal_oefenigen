import pytest
from code_oefeningenles import add,reverse_string,max_number,is_even,filter_even_numbers,concatenate_strings,is_prime


def test_add():
    assert add(3,5)


def test_reverse_string():
    assert reverse_string('ik ben robbe')

def test_max_number():
    assert max_number(15,25)

def test_is_even():
    assert is_even(8)

def test_filter_even_numbers():
    assert filter_even_numbers([1,2,5,8,9,10,45])

def test_concatenate_strings():
    assert concatenate_strings('ik ben robbe de clerck\n', 'ik ben de beste die er is\n')

def test_is_prime():
    assert is_prime(8)


@pytest.fixture(scope="function")
def function_scope_fixture():
    print ('function scope fixture setup')
    yield
    print('function scope fixture teardown')

@pytest.fixture(scope="class")
def class_scope_fixture():
    print ('class scope fixture setup')
    yield
    print('class scope fixture teardown')

@pytest.fixture(scope="module")
def module_scope_fixture():
    print ('module scope fixture setup')
    yield
    print('module scope fixture teardown')

@pytest.fixture(scope="session")
def session_scope_fixture():
    print ('session scope fixture setup')
    yield
    print('session scope fixture teardown')

