# %%
# pip install pytest

# %%
import pytest

# %%
def factorial(n):
  if n < 0:
    raise ValueError("Received negative input")
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

# %%
def test_factorial():
  assert factorial(0) == 1
  assert factorial(1) == 1
  assert factorial(2) == 2
  assert factorial(3) == 6


