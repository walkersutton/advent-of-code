def first_good(val):
  last = -1
  ret = ''
  base = ''
  same = False
  for ch in val:
    if same:
      ret += base
    elif int(ch) < last:
      same = True
      base = str(last)
      ret += base
    else:
      ret += ch
      last = int(ch)
  return ret

def possible_above(val):
  tot = 0
  for ii in range(1, len(val) + 1):
    cn = int(val[len(val) - ii])
    tot += (10 - cn) * ii
  return tot

mi = '387638'
ma = '919123'

mi = first_good(mi)
ma = first_good(ma)


miv = possible_above(mi)
mav = possible_above(ma)
print(abs(mav - miv))




