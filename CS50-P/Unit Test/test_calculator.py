from calculator import square #from calculator.py file
import pytest
#def main():
  #test_square()
#def test_square():
#  try:
#   assert square(2) == 4
#  except AssertionError:
#   print("2 was not equal to 4")
#  try:
#   assert square(3) == 9
#  except AssertionError:
#   print("3 was not equal to 9")
#if __name__ == "__main__":
#  main()

def test_positive():
  assert square(2) == 4
  assert square(3) == 9

def test_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_zero():
  assert square(0) == 0

def test_str():
  with pytest.raises(TypeError):
    square("cat")

#use python -m pytest to test

