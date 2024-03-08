def compute_heaviside(position):
  """Computes the value of the Heaviside step function at a given position."""
  if position >= 0:
    return 1
  elif position < 0:
    return 0
  else:
    print("Invalid value for x, please enter a real number")


if __name__ == "__main__":
  #Testing function at various values
  values = [-10, -25, 0, -5, 10]
  expected_values = [0, 0, 1, 0, 1]
  for i in range(len(values)):
    print(f'Test value of compute_heaviside(x) at value {values[i]} is {compute_heaviside(values[i])}, expected result is {expected_values[i]}')