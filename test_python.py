def test_m3():
    name="gayi"
    assert name.upper() == "GAYI", "failed"

def test_reverse():
    assert list(reversed([1,2,3,4])) == [4,3,2,1]

def test_prime():
    assert 37 in(num
                 for num in range(2,52)
                 if not any(num%div==0 for div in range(2,num)))



#py.test -k login -v


