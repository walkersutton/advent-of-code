infile = open('data.txt', 'r')
text_data = infile.readlines()
nums = [int(ele) for ele in text_data[0].split(',')]
cur = 0

nums[1] = 12
nums[2] = 2

while True:
  if nums[cur] == 1:
    nums[nums[cur + 3]] = nums[nums[cur + 1]] + nums[nums[cur + 2]]
  elif nums[cur] == 2:
    nums[nums[cur + 3]] = nums[nums[cur + 1]] * nums[nums[cur + 2]]
  elif nums[cur] == 99:
    break
  cur += 4

print(nums[0])
