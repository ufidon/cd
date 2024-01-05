import math


def n2d(n: str, b: int) -> float:
  pi = n.index('.')
  nl = len(n)
  s = 0.0
  for i in range(pi):
    s += int(n[i], b) * b**(pi-i-1)

  for i in range(nl-pi-1):
    s += int(n[i+pi+1], b) * b**(-i-1)
  return s


def i2b(i: int, b: int) -> str:
  s = ''
  while (i//b):
    if b == 16:
      s = hex(i % b)[2:] + s
    else:
      s = str(i % b) + s
    i = i//b

  if i != 0:
    if b == 16:
      s = hex(i % b)[2:] + s
    else:
      s = str(i % b) + s

  return s


def f2b(f: float, b: int, p: int = 20) -> str:
  s = ''
  while p > 0 and f > 0:
    f *= b
    d = math.floor(f)
    if b == 16:
      s += hex(d)[2:]
    else:
      s += str(d)

    if d > 0:
      f -= d

    p -= 1

  s = '0.' + s

  return s

def atable(b:int = 10):
  print("|", end='')
  for i in range(b):
    if b == 16:
      print(" %2x "%(i), end="|")
    else:
      print(" %2d "%(i), end="|")
  print("")

  print("|", end='')
  for i in range(b):
    print(" -- ", end="|")
  print("")
  
  for i in range(b):
    print("|", end='')
    for j in range(b):

      if b == 16:          
        print(" %2x "%(i+j), end="|")
      elif b == 8:
        print(" %2o "%(i+j), end="|")
      elif b == 2:
        print(" %2s "%(bin(i+j)[2:]), end="|")
      else:
        print(" %2d "%(i+j), end="|")
     
      # if j <= i:
      #   if b == 16:          
      #     print(" %2x "%(i+j), end="|")
      #   elif b == 8:
      #     print(" %2o "%(i+j), end="|")
      #   elif b == 2:
      #     print(" %2s "%(bin(i+j)[2:]), end="|")
      #   else:
      #     print(" %2d "%(i+j), end="|")
      # else:
      #   print("    ", end="|")
    print("")

def mtable(b:int = 10):
  print("|", end='')
  for i in range(b-1):
    if b == 16:
      print(" %2x "%((i+1)), end="|")
    else:
      print(" %2d "%((i+1)), end="|")
  print("")

  print("|", end='')
  for i in range(b-1):
    print(" -- ", end="|")
  print("")
  
  for i in range(b-1):
    print("|", end='')
    for j in range(b-1):
      if b == 16:          
        print(" %2x "%((i+1)*(j+1)), end="|")
      elif b == 8:
        print(" %2o "%((i+1)*(j+1)), end="|")
      elif b == 2:
        print(" %2s "%(bin((i+1)*(j+1))[2:]), end="|")
      else:
        print(" %2d "%((i+1)*(j+1)), end="|")
    
      # if j <= i:
      #   if b == 16:          
      #     print(" %2x "%((i+1)*(j+1)), end="|")
      #   elif b == 8:
      #     print(" %2o "%((i+1)*(j+1)), end="|")
      #   elif b == 2:
      #     print(" %2s "%(bin((i+1)*(j+1))[2:]), end="|")
      #   else:
      #     print(" %2d "%((i+1)*(j+1)), end="|")
      # else:
      #   print("    ", end="|")
    print("")


if __name__ == "__main__":
  # bs = ('1011101.11', '111.1', '100001.101')
  # for b in bs:
  #   print("%s->%g" % (b, n2d(b, 2)))

  # os = ('3423.12', '435.32', '7766.5544')
  # for o in os:
  #   print("%s->%g" % (o, n2d(o, 8)))

  # hs = ('fa.af', 'dead.beef', '5a6b.7c8d')
  # for h in hs:
  #   print("%s->%.22g" % (h, n2d(h, 16)))

  # print(i2b(153,8))
  # print(i2b(41,2))
  # print(i2b(57005, 16))
  # print(i2b(93, 2))
  # print(i2b(33, 2))
  # print(i2b(1811, 8))
  # print(i2b(285, 8))
  # print(i2b(4086, 8))
  # print(i2b(250, 16))
  # print(i2b(57005, 16))
  # print(i2b(23147, 16))
  

  # print(f2b(0.6875, 2))
  # print(f2b(0.513, 8))
  # print(f2b(.7458343505859375, 16))
  # print(f2b(.1, 2))

  # print(f2b(.75, 2))
  # print(f2b(.5, 2))
  # print(f2b(.625, 2))
  # print(f2b(.16, 8))
  # print(f2b(.406, 8))
  # print(f2b(.71, 8))
  # print(f2b(.72, 8))
  # print(f2b(.68359375, 16))
  # print(f2b(.4865264892578125, 16))

  # print(i2b(8, 2))
  # print(f2b(.25, 2))
  # print(i2b(70, 8))
  # print(f2b(.5, 8))
  # print(i2b(132, 16))
  # print(f2b(.4, 16))
  
  mtable(16)
  # atable(16)