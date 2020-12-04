infile = open('data.txt', 'r')
text_data = infile.readlines()
numbers = []
for element in text_data:
  numbers.append(int(element.strip()))

numbers.sort()
for ii in range(len(numbers) - 1):
  for jj in range(ii + 1, len(numbers)):
      if numbers[ii] + numbers[jj] == 2020:
        print(numbers[ii] * numbers[jj])
