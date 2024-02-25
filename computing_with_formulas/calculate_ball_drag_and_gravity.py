import math

drag_coefficient = 0.2 #unitless
air_density = 1.2 #kg/m^3
ball_radius = 0.11 #m
cross_area = (math.pi)*(ball_radius**2) #m^2
ball_velocity_soft = 10*(1000/(60**2)) #m/s, from km/h
ball_velocity_hard = 120*(1000/(60**2)) #m/s, from km/h
ball_mass = 0.43 #kg
graviational_acceleration = 9.8 #m/s^2

drag_force_soft = 0.5*drag_coefficient*air_density*cross_area*(ball_velocity_soft**2) #N
drag_force_hard = 0.5*drag_coefficient*air_density*cross_area*(ball_velocity_hard**2) #N
graviational_force = ball_mass*graviational_acceleration #N

force_ratio_soft = drag_force_soft/graviational_force #unitless
force_ratio_hard = drag_force_hard/graviational_force #unitless

print(f'Drag force for hard kick = {drag_force_hard:.1f}N, Drag force for soft kick = {drag_force_soft:.1e}N, Graviational force = {graviational_force:.1f}N, Force ratio for hard kick={force_ratio_hard:.1f}, Force ratio for soft kick={force_ratio_soft:.1e}')