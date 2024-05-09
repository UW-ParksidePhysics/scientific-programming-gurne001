from calculate_quadratic_fit import *
from calculate_bivariate_statistics import *
from fit_curve_array import *
from calculate_lowest_eigenvectors import *
from plot_data_with_fit import *
from read_two_columns_text import *


def parse_file_name(filename):
    split_filename=str.split(filename, '.')
    chemical_symbol = split_filename[0]
    crystal_symmetry_symbol = split_filename[1]
    density_functional_exchange_acronym = split_filename[2]
    return chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym


if __name__ == "__main__":
    chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym = parse_file_name("Au.Fm-3m.GGA-PBEsol.volumes_energies.dat")
    data = read_two_columns_text("Au.Fm-3m.GGA-PBEsol.volumes_energies.dat")
    statistics = calculate_bivariate_statistics(data)
    quadratic_fit_coefficients = calculate_quadratic_fit(data)