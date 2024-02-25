import math
#No unit conversion necessary for given values, instead comments indicate the variable name in function as listed in assignment
egg_mass_small = 47 #m (small)
egg_mass_large = 67 #m (large)
egg_specific_heat_capacity = 3.7 #c
egg_density = 1.038 #p
egg_thermal_conductivity = 5.4e-3 #k
boiling_water_temperature = 100 #Tw
original_egg_temperature_room_temperature = 20 #T0 (room temperature)
original_egg_temperature_cold = 4 #T0 (cold)
target_temperature = 70 #Ty

# Break original formula into two products, the rational expression and the portion within the natural log function
mass_term_small = egg_mass_small**(2/3) #m^2/3 (small)
mass_term_large = egg_mass_large**(2/3) #m^2/3 (large)
pi_term = (math.pi**2)*((4/3)*math.pi)**(2/3) #pi^2*(4pi/3)^2/3
#m^2/3*c*p^(1/3) (large)
term_1_numerator_large = mass_term_large*egg_specific_heat_capacity*(egg_density**(1/3))
#m^2/3*c*p^(1/3) (small)
term_1_numerator_small = mass_term_small*egg_specific_heat_capacity*(egg_density**(1/3))
#k*(pi term), matches denominator of first term in formula
term_1_denominator = egg_thermal_conductivity*pi_term
#calculate the rational expression that is the 1st term in the formula for small egg
term_1_small = term_1_numerator_small/term_1_denominator 
#calculate the rational expression that is the 1st term in the formula for large egg
term_1_large = term_1_numerator_large/term_1_denominator 


#Segment out the terms in the natural log portion of the formula for ease of calculation
ln_num_cold = original_egg_temperature_cold-boiling_water_temperature
ln_num_rmtemp = original_egg_temperature_room_temperature-boiling_water_temperature
ln_denom = target_temperature-boiling_water_temperature
ln_cold = math.log(0.76*(ln_num_cold/ln_denom))
ln_rmtemp = math.log(0.76*(ln_num_rmtemp/ln_denom))

#Take product of relevant rational/ln terms to calculate final result (in seconds) for all 4 situations of egg size/temp
time_large_cold_s = term_1_large*ln_cold
time_large_rmtemp_s = term_1_large*ln_rmtemp
time_small_cold_s = term_1_small*ln_cold
time_small_rmtemp_s = term_1_small*ln_rmtemp

#Convert seconds to minutes
time_large_cold_m = time_large_cold_s/60
time_large_rmtemp_m = time_large_rmtemp_s/60
time_small_cold_m = time_small_cold_s/60
time_small_rmtemp_m = time_small_rmtemp_s/60


print(f'It will take {time_large_cold_s:.2f} seconds, or {time_large_cold_m:.2f} minutes to cook a large egg from fridge temperature.')
print(f'It will take {time_large_rmtemp_s:.2f} seconds, or {time_large_rmtemp_m:.2f} minutes to cook a large egg from room temperature.')
print(f'It will take {time_small_cold_s:.2f} seconds, or {time_small_cold_m:.2f} minutes to cook a small egg from fridge temperature.')
print(f'It will take {time_small_rmtemp_s:.2f} seconds, or {time_small_rmtemp_m:.2f} minutes to cook a small egg from room temperature.')
