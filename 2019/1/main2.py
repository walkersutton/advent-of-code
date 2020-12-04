def fuel_of_fuel(mass):
  if mass <= 0:
    return 0
  else:
    fuel = mass // 3 - 2
    if fuel <= 0:
      return 0
    else:
      return fuel + fuel_of_fuel(fuel)

infile = open('data.txt', 'r')
text_data = infile.readlines()
total_fuel = 0
for element in text_data:
  total_fuel += fuel_of_fuel(int(element))

print(total_fuel)




