infile = open('data.txt', 'r')
text_data = infile.readlines()
base_nums = [int(ele) for ele in text_data[0].split(',')]

for noun in range(100):
  for verb in range(100):
    cur = 0
    nums = base_nums.copy()
    nums[1] = noun
    nums[2] = verb
    while True:
      if nums[cur] == 1:
        nums[nums[cur + 3]] = nums[nums[cur + 1]] + nums[nums[cur + 2]]
        cur += 4
      elif nums[cur] == 2:
        nums[nums[cur + 3]] = nums[nums[cur + 1]] * nums[nums[cur + 2]]
        cur += 4
      elif nums[cur] == 99:
        cur += 1
        break
    if nums[0] == 19690720:
      print(100 * noun + verb)
