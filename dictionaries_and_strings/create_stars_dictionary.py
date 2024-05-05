import sys

nearby_star_data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]


def convert_list_of_tuples(nearby_star_data):
    star_dictionary = {}
    for i in range(len(nearby_star_data)):
        star_dictionary[nearby_star_data[i][0]] = {"distance": nearby_star_data[i][1],
                                                   "apparent brightness": nearby_star_data[i][2],
                                                   "luminosity": nearby_star_data[i][3]}
    return star_dictionary


nearby_star_dictionary = (convert_list_of_tuples(nearby_star_data))


def print_star_information(star_name):
    try:
        output = (f'Star: {star_name}\n\tDistance (ly): {nearby_star_dictionary[star_name]["distance"]}\n'
                  f'\tApparent Brightness (m): {nearby_star_dictionary[star_name]["apparent brightness"]}\n'
                  f'\tLuminosity (L_sun): {nearby_star_dictionary[star_name]["luminosity"]}')
    except KeyError:
        print("Please use string 'Star Name' as input for function, for a star within the given star dictionary")
        sys.exit(1)
    return output


if __name__ == "__main__":
    print(print_star_information("Sirius A"))
    print(print_star_information("Sirius B"))