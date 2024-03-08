from math import sqrt
from cmath import sqrt as csqrt

def calculate_quadratic_roots(a, b, c):
  """Caclulates the roots of a quadratic equation."""
  discriminant = b**2 - 4*a*c
  roots = []
  if discriminant == 0:
    roots.append(-b / (2*a))
  elif discriminant > 0:
    roots.append((-b + sqrt(discriminant)) / (2*a))
    roots.append((-b - sqrt(discriminant)) / (2*a))
  elif discriminant < 0:
    roots.append((-b + csqrt(discriminant)) / (2*a))
    roots.append((-b - csqrt(discriminant)) / (2*a))
  return roots

if __name__ == "__main__":
  print(calculate_quadratic_roots(1, 2, 1))
  print(calculate_quadratic_roots(1, -2, -3))
  print(calculate_quadratic_roots(1, 0, 1))