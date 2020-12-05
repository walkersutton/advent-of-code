import math

infile = open('data.txt', 'r')
text_data = infile.readlines()
vals = []
for element in text_data:
  vals.append((element.strip()))

seat_ids = []

for seat in vals:

  mi = 0
  ma = 127
  for ii in range(7):
    if seat[ii] == 'F':
      ma -= math.ceil((ma - mi) / 2)
    else:
      mi += math.ceil((ma - mi) / 2)

  left = 0
  right = 7
  for ii in range(7, 10):
    val = seat[ii]
    if val == 'R':
      left += math.ceil((right - left) / 2)  
    else:
      right -= math.ceil((right - left) / 2)  

  seat_ids.append(ma * 8 + right)

print(max(seat_ids)) 
