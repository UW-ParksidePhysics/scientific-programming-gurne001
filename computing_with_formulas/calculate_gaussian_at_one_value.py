import math
mean = 0
standard_deviation = 2
input_value = 1

product_1 = 1/((math.sqrt(2*math.pi))*standard_deviation)
product_2 = ((input_value-mean)/standard_deviation)**2

gaussian = product_1*math.exp(-0.5*product_2)

print(f'Mean = {mean}, Standard Deviation = {standard_deviation}, Input Value = {input_value}, Gaussian = {gaussian:f}')