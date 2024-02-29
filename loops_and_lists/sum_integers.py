maximum_integer = 300
sum = 0
for i in range(1, maximum_integer + 1):
  sum += i

formula_sum = (maximum_integer*(maximum_integer+1))/2

print(f'n = {maximum_integer}')
print(f'sum(1, {maximum_integer}) = {sum}')
print(f'n(n+1)/2 = {formula_sum:.0f}')