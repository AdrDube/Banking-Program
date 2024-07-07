import pytest
from banking import convert, balance, withdrawal, deposit, new_file

def test_convert():
    assert int(convert(90.00,"CAD", "USD")/10)==6
    assert int(convert(90, "EUR", "CAD")/10)==13

    with pytest.raises(SystemExit):
        assert convert(90.00, "ZIM", "CAD")
    with pytest.raises(SystemExit):
        assert convert(90,"USD", "ZIM")

#Uses an already existing A.csv with the initial balance of 100
def test_balance():
    assert new_file("A.csv")==None
    assert int(balance("A.csv"))== 100
    with pytest.raises(FileNotFoundError):
        assert balance("x.txt")
def test_withdrawal():
    assert int(withdrawal(50, "A.csv")) == 50
    assert int(withdrawal(60, "A.csv"))==-10
def test_deposit():
    assert int(deposit(60, "A.csv"))== 50
    assert int(deposit(50, "A.csv")) == 100
    
