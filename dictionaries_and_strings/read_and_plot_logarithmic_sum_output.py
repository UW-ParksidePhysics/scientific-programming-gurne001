import matplotlib.pyplot as plt


def parse_sum_output(file):
    file = open(file, 'r')
    epsilon_table = file.readlines()[24:]
    tolerances = []
    errors = []
    maximum_indices = []
    for line in epsilon_table:
        adjusted_line = str.replace(line, ",", ":").replace("=", ":")
        contents = adjusted_line.split(":")
        tolerances.append(contents[1])
        errors.append(contents[3])
        maximum_indices.append(contents[5])
    for i in range(len(tolerances)):
        tolerances[i] = float(tolerances[i][1:])
        errors[i] = float(errors[i][1:])
        maximum_indices[i] = int(maximum_indices[i][:-1])
    return tolerances, errors, maximum_indices


def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    plot_1 = plt.semilogy(maximum_indices, tolerances, label="Tolerance")
    plot_2 = plt.semilogy(maximum_indices, errors, label="Error")
    return plot_1, plot_2


if __name__ == "__main__":
    plot_logarithmic_sum_error(parse_sum_output("logarithmic_sum.out")[0], parse_sum_output("logarithmic_sum.out")[1], parse_sum_output("logarithmic_sum.out")[2])
    plt.xlabel("Maximum Indices")
    plt.title("Error and Tolerance for Logarithmic Sum")
    plt.legend()
    plt.show()
