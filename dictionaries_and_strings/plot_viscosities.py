import numpy
import matplotlib.pyplot


def parse_viscosity_data(file):
    file = open(file, 'r')
    viscosity_table = file.readlines()[9:17]
    viscosity_dictionary = {}
    for line in viscosity_table:
        adjusted_line = line.split()
        if len(adjusted_line) == 4:
            viscosity_dictionary[adjusted_line[0]] = {"viscosity": float(adjusted_line[1]),
                                                      "reference_temperature": float(adjusted_line[2]),
                                                      "reference_viscosity": float(adjusted_line[3])}
        else:
            viscosity_dictionary[adjusted_line[0] + ' ' + adjusted_line[1]] = {"viscosity": float(adjusted_line[2]),
                                                                               "reference_temperature": float(adjusted_line[3]),
                                                                               "reference_viscosity": float(adjusted_line[4])}
    return viscosity_dictionary


def calculate_viscosity(temperature, gas, viscosity_data):
    reference_viscosity = viscosity_data[gas]["reference_viscosity"]
    viscosity = viscosity_data[gas]["viscosity"]
    reference_temperature = viscosity_data[gas]["reference_temperature"]
    function = reference_viscosity*((reference_temperature-viscosity)/(temperature+viscosity))*((temperature/reference_temperature)**1.5)
    return function


if __name__ == "__main__":
    temp_values = numpy.linspace(223, 373, 300)
    air_values = (calculate_viscosity(temp_values, "air", parse_viscosity_data("viscosity_of_gases.dat")))
    carbon_dioxide_values = (calculate_viscosity(temp_values, "carbon dioxide", parse_viscosity_data("viscosity_of_gases.dat")))
    hydrogen_values = (calculate_viscosity(temp_values, "hydrogen", parse_viscosity_data("viscosity_of_gases.dat")))

    matplotlib.pyplot.plot(temp_values, air_values, label="Air")
    matplotlib.pyplot.plot(temp_values, carbon_dioxide_values, label="Carbon Dioxide")
    matplotlib.pyplot.plot(temp_values, hydrogen_values, label="Hydrogen")
    matplotlib.pyplot.xlabel("Temperature (K)")
    matplotlib.pyplot.ylabel("Viscosity")
    matplotlib.pyplot.title("Viscosity of Gases")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()
