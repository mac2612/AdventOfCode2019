def allfuel(amt):
    fuel = int(int(amt) / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + allfuel(fuel)

with open('input.txt', 'r') as fp:
    fueltotal = 0
    fuel_moduleonly = 0
    for line in fp:
      mass = int(line)
      fueltotal += allfuel(mass)
      fuel_moduleonly += int(int(mass) / 3) - 2
    print(f'FuelOnFuel = {fueltotal}')
    print(f'Modules Only = {fuel_moduleonly}')
