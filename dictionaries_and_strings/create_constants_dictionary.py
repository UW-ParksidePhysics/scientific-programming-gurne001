def parse_constants_file(filename):

    constant_dictionary = {}
    file = open(filename, 'r')
    file.readline()
    file.readline()
    for line in file:
        contents = line.split()
        if len(contents) == 4:
            constant_name = contents[0] + ' ' + contents[1]
        if len(contents) == 5:
            constant_name = contents[0] + ' ' + contents[1] + ' ' + contents[2]
        constant_value = float(contents[-2])
        constant_dictionary[constant_name] = constant_value
    file.close()
    return constant_dictionary


if __name__ == "__main__":
    print(parse_constants_file("constants.txt"))



