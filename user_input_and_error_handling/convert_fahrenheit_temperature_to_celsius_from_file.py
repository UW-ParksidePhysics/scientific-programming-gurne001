def temp_f_to_c(x):
  return (x - 32) * (5 / 9)
  

data = open('user_input_and_error_handling/temperature.txt', 'r')

data.readline() #skip 1st line
data.readline() # skip second line
for line in data:
  words = line.split() #split third line into 'words'

temperature = float(words[2]) #desired value is 3rd object in 'words', pull as a float
temperature_celsius = temp_f_to_c(temperature)

print(f'{temperature} degrees Fahrenheit is {temperature_celsius} degrees Celsius')