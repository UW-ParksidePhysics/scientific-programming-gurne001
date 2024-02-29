def spring_potential_energy(k, y, yeq, m, g):
    return (k * (y - yeq) ** 2) * 0.5 + m * g * y

print (spring_potential_energy(float(input("Spring constant = ?")), float(input('Y?')), float(input('Y equilibrium?')), float(input('Mass?')), 9.8))