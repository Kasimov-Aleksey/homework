from main import check as c

def test(a, b):
    c(a, b)
    host = a+b
    assert host == c(a, b)


test(10, 30)
test(14, 34)
test(41, 43)
