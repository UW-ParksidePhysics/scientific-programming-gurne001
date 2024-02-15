life_expectancy_in_seconds = 73.5*365*24*60*60
one_billion = 10**9
print(life_expectancy_in_seconds, end=" ") #end=" " makes it so that the next print statement will be on the same line
print(one_billion, end=" ")

if life_expectancy_in_seconds >=one_billion:
  print("Yes, a newborn can expect to live more than a billion seconds")
else:
  print("No, a newborn can expect to live less than a billion seconds")
