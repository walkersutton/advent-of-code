infile = open('data.txt', 'r')
text_data = infile.readlines()
numbers = []
for element in text_data:
  numbers.append(int(element.strip()))

numbers.sort()
for ii in range(len(numbers) - 2):
  for jj in range(ii + 1, len(numbers) - 1):
    for kk in range(jj + 1, len(numbers)):
      val = numbers[ii] + numbers[jj] + numbers[kk] 
      if val == 2020:
        print(val)
      elif val > 2020:
        break
