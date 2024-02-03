import pytest
from ..code.new_code import Address
from ..code.errors import *

def test_call_address_class():
    address=Address("straat","apen","2000","belgie")



@pytest.mark.parametrize("straat, city, zip_code, country",[("straat","apen",2000,"belgie")])
def test_string_method_class(street,city,zip_code,country):
    address=Address("straat","apen","2000","belgie")
    assert address.__str__()== f"{street},{city},{zip_code},{country}"

def test_address_street_empty():
    with pytest.raises(EmptyStringError):
        address=Address("","apen","2000","belgie")