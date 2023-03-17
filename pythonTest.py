import pytest

def test_m1():
    a=2
    b=1
    assert a==b, "failed"
    assert (a-b)==1, "failed"

def test_m2():
    assert True

def test_m3():
    name="gayi"
    assert name.upper() == "GAYI", "failed"

def test_reverse():
    assert list(reversed([1,2,3,4])) == [4,3,2,1]

def test_prime():
    assert 37 in(num
                 for num in range(2,52)
                 if not any(num%div==0 for div in range(2,num)))






