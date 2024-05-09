from calculate_quadratic_fit import *
from calculate_bivariate_statistics import *
from fit_curve_array import *
from calculate_lowest_eigenvectors import *
from plot_data_with_fit import *
from read_two_columns_text import *
from equations_of_state import fit_eos
from convert_units import *
from annotate_plot import *
import sys
import matplotlib.pyplot as plt
from numpy import amin, amax, min, max
from datetime import *


def parse_file_name(filename):
    try:
        split_filename=str.split(filename, '.')
        chemical_symbol = split_filename[0]
        crystal_symmetry_symbol = split_filename[1]
        density_functional_exchange_acronym = split_filename[2]
    except TypeError:
        print("Please input valid filename as string")
        sys.exit(1)
    except IndexError:
        print("Please input valid filename (separated by '.'s) as string")
        sys.exit(1)
    return chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym


if __name__ == "__main__":
    chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym = parse_file_name("Au.Fm-3m.GGA-PBEsol.volumes_energies.dat")
    data = read_two_columns_text("Au.Fm-3m.GGA-PBEsol.volumes_energies.dat")
    statistics = calculate_bivariate_statistics(data)
    minimum_x = statistics[2]
    maximum_x = statistics[3]
    minimum_y = statistics[4]
    maximum_y = statistics[5]
    quadratic_fit_coefficients = calculate_quadratic_fit(data)
    eos_fit_data, eos_parameters = fit_eos(data[0], data[1], quadratic_fit_coefficients, "Murnaghan")
    # Note: eos_fit_data is an array of "y-values"(energies) corresponding to the "x-values"(volumes) in data[0]
    converted_values = [convert_units(data[0], "atomic_volume", "cubic_angstrom"), convert_units(data[1], "atomic_energy", "electron_volts"),
                        convert_units(eos_fit_data, "atomic_energy", "electron_volts")]
    converted_data = [converted_values[0], converted_values[1]]
    converted_statistics = calculate_bivariate_statistics(converted_data)
    converted_xmin = converted_statistics[2]
    converted_xmax = converted_statistics[3]
    converted_ymin = converted_statistics[4]
    converted_ymax = converted_statistics[5]
    fit_curve = [linspace(converted_xmin, converted_xmax, 50), converted_values[2]]
    plot_data_with_fit(converted_data, fit_curve, "bo", "black")
    x_axis_min = 0.9*converted_xmin
    x_axis_max = 1.1*converted_xmax
    # y_axis_min = 0.9*converted_ymin
    # y_axis_max = 1.1*converted_ymax
    plt.xlim(x_axis_min, x_axis_max)
    # plt.ylim(y_axis_min, y_axis_max)
    # Fundamental issue with Parker's request to scale ylims by 10% of min/max y-values,
    # the scale of those values mean that the 10% scaling makes the graph unreadable
    date = date(2024, 5, 9).isoformat()
    annotations_dictionary = {f'{chemical_symbol}':
                                  {"position": (2,-5.085477e4), "alignment": ["left", "bottom"], "fontsize": 12},
                              f'{crystal_symmetry_symbol}':
                                  {"position": (2.45, -5.0856e4), "alignment": ["left", "bottom"], "fontsize": 12},
                              f'K0 = {abs(round(quadratic_fit_coefficients[1],2))} GPa':
                                  {"position": (2.4, -5.08555e4), "alignment": ["left", "bottom"], "fontsize": 12},
                              f'V0 = {round(converted_data[0][3], 2)} A3/Atom':
                                  {"position": (2.26, -5.0858365e4), "alignment": ["left", "top"], "fontsize": 8},
                              f'Created by Tyler Gurney {date}':
                                  {"position": (1.8, -5.085875e4), "alignment": ["left", "top"], "fontsize": 12}}

    annotate_plot(annotations_dictionary)
    plt.title(f"Murnaghan Equation of State for {chemical_symbol} in DFT {density_functional_exchange_acronym}")
    plt.show()