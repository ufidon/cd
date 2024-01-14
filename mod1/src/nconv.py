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


def i2b(i: int, b: int, prt=False) -> str:
  s = ''
  while (i//b):
    if b == 16:
      s = hex(i % b)[2:] + s
    else:
      s = str(i % b) + s
    ip = i
    i,r = i//b, i%b
    print(f'{ip}={b}×{i}+{r}') if prt==True else None

  if i != 0:
    if b == 16:
      s = hex(i % b)[2:] + s
    else:
      s = str(i % b) + s
    print(f'{i}={b}×0') if prt==True else None

  return s


def f2b(f: float, b: int, p: int = 20, prt=False) -> str:
  s = ''
  while p > 0 and f > 0:
    pf = f
    f *= b
    d = math.floor(f)
    print(f'{pf}×{b}={f}') if prt==True else None
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


def b2g(n:int, w:int=4)->str:
  f = '{:0' +str(w) + 'b}'
  b = f.format(n)
  g = b[0]
  t = ''
  
  for k in range(w-1):
    t = str(int(b[w-1-k]) ^ int(b[w-2-k])) + t
  
  g += t
  return g

def g2b(n:int, w:int=4)->str:
  f = '{:0' +str(w) + 'b}'
  g = f.format(n)
  b = g[0]
  t = ''
  
  for k in range(w-1):
    o = 0
    for l in range(w-k):
      o ^= int(g[l])
    t = str(o) + t
  
  b += t
  return b  

def bcd(n:str)->str:
  s = ''
  for d in n:
    s += f'{int(d):04b} ' if d.isdigit() else d
  return s

if __name__ == "__main__":
  # ng = []
  # for n in range(16):
  #   g = b2g(n)
  #   m = int(g,2)
  #   ng.append(m)
  #   b = g2b(m)
  #   nb = int(b,2)
  #   print(f'{nb:02d} {b} {g} {m:02d}')
  
  # print(g2b(12))
  
  # bs = ('1011101.11', '111.1', '100001.101')
  # for b in bs:
  #   print("%s->%g" % (b, n2d(b, 2)))

  # os = ('3423.12', '435.32', '7766.5544')
  # for o in os:
  #   print("%s->%g" % (o, n2d(o, 8)))

  # hs = ('fa.af', 'dead.beef', '5a6b.7c8d')
  # for h in hs:
  #   print("%s->%.22g" % (h, n2d(h, 16)))

  # print(i2b(153,8, True))
  # print(i2b(512,8, True))
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
  

  # print(f2b(0.6875, 2, 20, True))
  # print(f2b(0.513, 8, 20, True))
  # print(f2b(.7458343505859375, 16))
  # print(f2b(.1, 2, 20, True))
  # print(i2b(132, 16, True))
  # print(f2b(.7, 16, 20, True))
  # print(i2b(494//17,8))
  # print(f2b(494/17-494//17,8))
  # print(n2d('35.0360741703607417',8))
 
  # print(i2b(48879//174,16))
  # print(f2b(48879/174-48879//174,16))
  # print(n2d('118.e9ee58469ee',16))  

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
  
  # mtable(16)
  # atable(16)
  
  # print(bcd('663'))
  # print(f2b(.14,2,500))
  # print(n2d('0.00100011110101110000101000111101011100001010001111011',2))
  # 0.000000101111100000110111101101001010001000110011100111
  
  t = ['5201314', '314.125', '2023.0116']
  for x in t:
    print(f'{bcd(x)}')
  
  n = [5201314, 314, 2023]
  for k in n:
    print(f'{i2b(k, 2)}')
    
  f = [.125, .0116]
  for x in f:
    print(f'{f2b(x,2,500)}')