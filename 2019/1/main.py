infile = open('data.txt', 'r')
text_data = infile.readlines()
total_fuel = 0
for element in text_data:
  total_fuel += (int(element) // 3 - 2)

print(total_fuel)




