infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append(element.split())

cou = 0
for policy in vals:
  nums = policy[0].split('-')
  mi = int(nums[0])
  ma = int(nums[1])
  if (policy[2][mi - 1] == policy[1][0]) or (policy[2][ma - 1] == policy[1][0]):
    if not ((policy[2][mi - 1] == policy[1][0]) and (policy[2][ma - 1] == policy[1][0])):
      cou += 1
print(cou)
