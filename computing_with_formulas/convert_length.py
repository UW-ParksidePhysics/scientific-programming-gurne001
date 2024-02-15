distance_kilometers = 17.2
distance_meters = distance_kilometers*1000
distance_centimeters = distance_meters*100
distance_inches = distance_centimeters/2.54
distance_feet = distance_inches/12
distance_yards = distance_feet/3
distance_miles = distance_yards/1760

unit_list = ["inches", "feet", "yards", "miles"]
home_distance = [distance_inches, distance_feet, distance_yards, distance_miles]
for i in range(len(unit_list)):
  home_distance[i] = f'{home_distance[i]:.2f}' #rounds to 2 decimal places
  home_distance[i] = str(home_distance[i]) + unit_list[i] #adds unit using string +

print(home_distance)