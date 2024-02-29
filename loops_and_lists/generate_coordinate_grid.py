a = 1
b = 2
n = 20
h = (b - a) / n

list_for = []
for i in range(1,n+1):
  list_for.append(round(a + i * h,2))

list_comprehension = [round(a + i * h,2) for i in range(1,n+1)]

print(f'For x in [{a}, {b}] with {n} intervals, the interval length is h = {h:0.3f}, and \nUsing a for loop:\nx = {list_for}\nUsing list comprehension:\nx = {list_comprehension}')