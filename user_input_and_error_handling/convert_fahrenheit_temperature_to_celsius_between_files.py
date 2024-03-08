def temp_fahrenheit_to_celsius(x):
  return (x - 32) * (5 / 9)


infile = open('user_input_and_error_handling/temperature_2.txt', 'r')

infile.readline() #skip first line
infile.readline() #skip 2nd line
fahrenheit_temperatures = []
for line in infile:
  words = line.split() #split each line into words
  temperature = float(words[2]) #pulls desired obj as float
  fahrenheit_temperatures.append(temperature) #appends obj to empty list for later use

celsius_temperatures = []
for i in range(len(fahrenheit_temperatures)):
  celsius_temperatures.append(round(temp_fahrenheit_to_celsius(fahrenheit_temperatures[i]),2))

#Now must print output from lists into file w/ 2 columns, F on left, C on right

outfile = open('user_input_and_error_handling/temperature_2_output.txt', 'w')
outfile.write('F \t\t C \n') #header/label for columns
for i in range(len(fahrenheit_temperatures)):
  outfile.write(f'{fahrenheit_temperatures[i]} \t {celsius_temperatures[i]}') #iterates thru lists of temps, printing matching items in 2 columns
  outfile.write('\n') #adds new line for ever new pair

outfile.close()