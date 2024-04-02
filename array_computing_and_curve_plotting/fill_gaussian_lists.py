from numpy import sqrt, pi, exp
#Importing functions from numpy instead of math allows for the gaussian function to perform array computations in later assignments

def gaussian(position):
  exponent = -1 * (position ** 2) / 2
  product = 1 / (sqrt(2 * pi))
  return product * exp(exponent)

if __name__ == "__main__":
  positions = []
  for i in range(0, 41):
    positions.append(-4+(8/40)*i)
  gaussian_values = []
  for i in range(len(positions)):
    gaussian_values.append(gaussian(positions[i]))
  print(gaussian_values)