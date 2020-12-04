infile = open('data.txt', 'r')
text_data = infile.readlines()
numbers = []
for element in text_data:
  numbers.append(int(element.strip()))

numbers.sort()
for ii in range(len(numbers) - 2):
  for jj in range(ii + 1, len(numbers) - 1):
    for kk in range(jj + 1, len(numbers)):
      if numbers[ii] + numbers[jj] + numbers[kk] == 2020:
        print(numbers[ii] * numbers[jj] * numbers[kk])
