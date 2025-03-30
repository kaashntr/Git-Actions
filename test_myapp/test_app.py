from myapp.app import add, subtract, multiply, divide, calculator

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-3, -5) == -8

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0
    assert subtract(-5, -3) == -2

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(0, 5) == 0
    assert multiply(-3, 5) == -15
    assert multiply(-3, -5) == 15

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(0, 5) == 0
    assert divide(-6, 2) == -3
    assert divide(5, 0) == "Cannot divide by zero!"