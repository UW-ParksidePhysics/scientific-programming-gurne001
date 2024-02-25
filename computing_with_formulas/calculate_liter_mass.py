def kg_per_m3_to_g_per_cm3(X): #converts densities from kg/m^3 to g/cm^3
  return X*(1000/(100**3))

def density_to_mass_per_liter(X): #converts g/cm^3 to g/liter
  return (X*1000)

density_iron = kg_per_m3_to_g_per_cm3(7870)
density_air = kg_per_m3_to_g_per_cm3(1.2)
density_gasoline = .755
density_ice = kg_per_m3_to_g_per_cm3(916.7)
density_human = 1.096
density_silver = kg_per_m3_to_g_per_cm3(10500)
density_platinum = kg_per_m3_to_g_per_cm3(21450)

density_list = [density_iron, density_air, density_gasoline, density_ice, density_human, density_silver, density_platinum]

mass_list = []
for i in range(len(density_list)):
  mass_list.append(density_to_mass_per_liter(density_list[i])) #converts to g/liter for all elements of density list

name_list = ["Iron", "Air", "Gasoline", "Ice", "Human", "Silver", "Platinum"]

for i in range(len(mass_list)):
  mass_list[i] = f'{name_list[i]}: {mass_list[i]:.1f}' + " g/liter" #creates string w/ desired output incl units
  print(mass_list[i])