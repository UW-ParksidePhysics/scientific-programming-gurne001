import sys
from scipy.constants import e, epsilon_0, m_e, h
import numpy


def convert_units(value, convert_from, convert_to):
    try:
        convert_from_list = ["atomic_volume", "cubic_angstrom", "atomic_energy", "electron_volt", "atomic_modulus", "gigapascal"]
        if convert_from in convert_from_list:
            bohr_to_angstrom = 0.529177210903
            rydeberg_to_ev = 13.605693122994
            ryd_b3_to_gpa = ((rydeberg_to_ev*e)/((bohr_to_angstrom**3)*10e-30))*10e-9
            if convert_from == "atomic_volume":
                converted_value = value*(bohr_to_angstrom**3)
            elif convert_from == "cubic_angstrom":
                converted_value = value*(1/(bohr_to_angstrom)**3)
            elif convert_from == "atomic_energy":
                converted_value = value*rydeberg_to_ev
            elif convert_from == "electron_volt":
                converted_value = value*(1/rydeberg_to_ev)
            elif convert_from == "atomic_modulus":
                converted_value = value*ryd_b3_to_gpa
            elif convert_from == "gigapascal":
                converted_value = value*(1/ryd_b3_to_gpa)
        else:
            raise TypeError
    except TypeError:
        print("Please input valid atomic unit for conversion, valid number for value input")
        print("Valid inputs:\n"
              f"{convert_from_list}")
        sys.exit(1)
    return converted_value


if __name__ == "__main__":
    print(f"1 cubic bohr = "
          f"{convert_units(1, 'atomic_volume', 'cubic_angstrom')} cubic angstroms per atom\n")
    print(f"1 rydberg per atom equals "
          f"{convert_units(1, 'atomic_energy', 'electron_volt')} electron volts per atom\n")
    print(f"1 rydberg per cubic bohr equals "
          f"{convert_units(1, 'atomic_modulus', 'gigapascals')} gigapascals")
