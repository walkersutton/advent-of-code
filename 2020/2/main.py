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
  if mi <= policy[2].count(policy[1][0]) <= ma:
    cou += 1
print(cou)
