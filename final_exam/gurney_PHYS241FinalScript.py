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
from generate_matrix import *


def parse_file_name(filename):
    """Takes filename of assigned dataset and returns the chemical symbol, symmetry symbol, and DFE acronymn as strings"""
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
    display_plot = True
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
    y_axis_min = -5.0859e4
    y_axis_max = -5.08535e4
    plt.xlim(x_axis_min, x_axis_max)
    plt.ylim(y_axis_min, y_axis_max)
    # Fundamental issue with Parker's request to scale ylims by 10% of min/max y-values,
    # the scale of those values mean that the 10% scaling makes the graph unreadable
    date = date(2024, 5, 9).isoformat()
    math_chemical_symbol = r'$Au$'
    math_modulus = r'$K_0$ = ' + f'{round(eos_parameters[2],2)} GPa'
    math_volume = r'$V_0$ = ' + f'{round(converted_data[0][3], 2)} ' + r'$\mathrm{\AA}^3$/atom'
    math_symmetry_symbol = r'$Fm\bar3m$'
    math_xlabel = r'$V = \mathrm{\AA}^3$/atom'
    math_ylabel = r'$E = eV$/atom'
    plt.xlabel(math_xlabel)
    plt.ylabel(math_ylabel)
    annotations_dictionary = {f'{math_chemical_symbol}':
                                  {"position": (2,-5.085385e4), "alignment": ["left", "bottom"], "fontsize": 12},
                              f'{math_symmetry_symbol}':
                                  {"position": (2.45, -5.08545e4), "alignment": ["left", "bottom"], "fontsize": 12},
                              f'{math_modulus}':
                                  {"position": (2.4, -5.0854e4), "alignment": ["left", "bottom"], "fontsize": 12},
                              f'{math_volume}':
                                  {"position": (2.26, -5.08585e4), "alignment": ["left", "top"], "fontsize": 8},
                              f'Created by Tyler Gurney {date}':
                                  {"position": (1.8, -5.08595e4), "alignment": ["left", "top"], "fontsize": 10}}

    annotate_plot(annotations_dictionary)
    plt.title(f"Murnaghan Equation of State for {chemical_symbol} in DFT {density_functional_exchange_acronym}")
    v0_marker_data = [[converted_data[0][5], converted_data[0][5]], [y_axis_min, converted_data[1][5]]]
    plt.plot(v0_marker_data[0],v0_marker_data[1], color="black", linestyle="--")
    if display_plot:
        plt.show()
    else:
        plt.savefig("Gurney.Au.Fm-3m.GGA-PBEsol.MurnaghanEquationOfState.png")

    # Part 2: Matrix Graph code
    matrix = generate_matrix(-10, 10, 100, 'harmonic', 4)
    low_values, low_vectors = calculate_lowest_eigenvectors(matrix, 5)
    eigenvectors = [low_vectors[2], low_vectors[3], low_vectors[4]]
    eigenvalues = [low_values[2], low_values[3], low_values[4]]
    max_components = [amax(eigenvectors[0]), amax(eigenvectors[1]), amax(eigenvectors[2])]
    max_value = amax(max_components)
    y2_lim_max = 2*max_value
    y2_lim_min = -2*max_value
    colors = ["red", "green", "blue"]
    x_grid = linspace(-10, 10, 100)
    figure2, axes2 = plt.subplots()
    for i in range(0,3):
        label = fr'$\psi_{i+2}$, $E_{i+2}$ = {round(eigenvalues[i],3)}a.u.'
        axes2.plot(x_grid, eigenvectors[i], label=label, color=colors[i])
    axes2.set(xlabel='x [a.u.]', ylabel=r'$\psi_n (x)$[a.u.]',
              title="Select Wavefunctions for Harmonic Potential on a Spatial Grid of 100 Points")
    plt.axhline(color="black")
    plt.ylim(y2_lim_min, y2_lim_max)
    plt.legend(loc="upper right")
    annotations_dictionary_2 = {f'Created by Tyler Gurney {date}':
                                  {"position": (-13.5, -.325), "alignment": ["left", "top"], "fontsize": 10}}
    annotate_plot(annotations_dictionary_2)
    if display_plot:
        plt.show()
    else:
        plt.savefig("Gurney.Harmonic.Eigenvector234.png")
