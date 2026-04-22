import simple_math
import pytest
math = simple_math.SimpleMath()
@pytest.fixture
def square():
    return math.square
def test_square_positive_int_number(square):
    assert square(5) == 25
def test_square_negative_int_number(square):
    assert square(-5) == 25
def test_square_positive_null(square):
    assert square(0) == 0
def test_square_negative_null(square):
    assert square(-0) == 0
def test_square_positive_float_number(square):
    assert square(5.5) == 30.25
def test_square_negative_float_number(square):
    assert square(-5.5) == 30.25
@pytest.fixture
def cube():
    return math.cube
def test_cube_positive_int_number(cube):
    assert cube(5) == 125
def test_cube_negative_int_number(cube):
    assert cube(-5) == -125
def test_cube_positive_null(cube):
    assert cube(0) == 0
def test_cube_negative_null(cube):
    assert cube(-0) == -0
def test_cube_positive_float_number(cube):
    assert cube(5.5) == 166.375
def test_cube_negative_float_number(cube):
    assert cube(-5.5) == -166.375