def exchange1(a,y):
  c=a[y]
  a[y]=a[y+1]
  a[y+1]=c
  d=''.join(a)
  return d
def exchange_without_tail(ori,b,c):
############################################ 1 pair
  jizu = c//2
  for i in range(len(ori) - 1):
    a = []
    a = a + ori 
    yang = [] + a 
    d = exchange1(a,i)
    b.append(d)
############################################# 2 pairs
  for i in range(1,c):
    linshi =[] + list(b[i])
    for z in range(i+1,c-1):        
      linshi1 = [] + linshi
      d = exchange1(linshi1,z)
      b.append(d)
  qianshu = c
  houshu = len(b)
############################################## 3 pairs
  for i in range(qianshu,houshu):
    linshi =[] + list(b[i])
    shiqian = 0
    for po in range(c):
      if yang[po] != linshi[po]:
        shiqian = po
    for z in range(shiqian+1,c-1):
      linshi1 = [] + linshi
      d = exchange1(linshi1,z)
      b.append(d)
################################################ many pairs
  for noneed in range(jizu-3):  
    qianshu = houshu
    houshu = len(b)
    for i in range(qianshu,houshu):
      linshi =[] + list(b[i])
      shiqian = 0
      for po in range(c):
        if yang[po] != linshi[po]:
          shiqian = po
      for z in range(shiqian+1,c-1):
        linshi1 = [] + linshi
        d = exchange1(linshi1,z)
        b.append(d)
  return b



class Wedding: 
  def __init__(self):
    pass
  def shuffle(self, guests):
    ############################################ initial
    ori = guests   ###input characters you want to arrange
    apai = []
    apai.append(ori)
    ori = list(ori)
    c = len(ori)
    ############################################# tail arrange
    ori1 = []
    bpai = []
    for i in range(1,len(ori)-1):
      ori1.append(ori[i])
    bpai.append(''.join(ori1))
    c1 = len(ori1)
    d = exchange_without_tail(ori1,bpai,c1)
    for i in range(len(d)):
      d[i] = ori[c-1] + d[i] + ori[0]
    ############################################# middle arrange
    b = exchange_without_tail(ori,apai,c)
    for i in range(len(d)):
      b.append(d[i])
    #############################################clockwise and counterclockwise
    e = []
    a = [] + ori
    zan = a[0]
    for i in range(c-1):
      a[i]=a[i+1]
    a[c-1] = zan    
    f=''.join(a)
    e.append(f)
    a = [] + ori
    zan = a[c-1]
    for i in range(c-1,0,-1):
      a[i]=a[i-1]
    a[0] = zan    
    f=''.join(a)
    e.append(f)    
    for i in range(len(e)):
      b.append(e[i])
    if len(ori) == 2:
      b.pop(2)
      b.pop(2)
      b.pop(2)
    return b

  def shuffle_barriers(self, guests, bars):
    ori = guests
    ori = list(ori) 
    jieguo = []
    for i in range(len(bars)):
      bars[i] += i
    c = []
    jishu = 0
    for i in range(len(ori)+len(bars)):
      c.append(0)
    for i in range(len(c)):
      if i in bars:
        c[i] = '|'
        jishu += 1
      else:
        c[i] = ori[i-jishu]
    ###################################################
    d = []
    for i in range(len(bars)+1):
      d.append([])
    z = 0
    for i in range(len(c)):
      if c[i] == '|':
        z += 1
      else:
        d[z].append(c[i])              ##d wei 2d list 
    ######################################
    b = []
    for i in range(len(bars)+1):
      b.append([])
    for p in range(len(d)):  
      b[p].append(''.join(d[p]))
      changdu = len(d[p])
      b[p] = exchange_without_tail(d[p],b[p],changdu)
    #########################################ZhnegHe1
    result = [[]]
    part1 = []
    for pool in b:
      tmp = []
      for x in result:
        for y in pool:
          tmp.append(x+[y])
      result = tmp   
    for i in range(len(result)):
      part1.append('|'.join(result[i]))
    jieguo.extend(part1)
    ###############################################################tail arrange
    if bars[0] != 0:
      shou = d[0].pop(0)
      wei = d[len(d)-1].pop(len(d[len(d)-1])-1)
      b = []
      for i in range(len(bars)+1):
        b.append([])
      for p in range(len(d)):  
        b[p].append(''.join(d[p]))
        changdu = len(d[p])
        b[p] = exchange_without_tail(d[p],b[p],changdu)
      result = [[]]
      part1 = []
      for pool in b:
        tmp = []
        for x in result:
          for y in pool:
            tmp.append(x+[y])
        result = tmp   
      for i in range(len(result)):
        part1.append(wei + '|'.join(result[i]) + shou)
      jieguo.extend(part1)
    return jieguo
######################################################################################################
def  show_result(v, partial=False,ind=None):
  v.sort()
  if not partial:
    print("",len(v),"\n".join(v),sep="\n")
  else:
    print("",len(v),v[ind],sep="\n")



def standard_tests():
  standard = Wedding()
  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("WXYZ")
  show_result(res)

  res = standard.shuffle_barriers("xyz", [0])
  show_result(res)
  
  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("abcdefXY")
  show_result(res)

  res = standard.shuffle_barriers("abcDEFxyz", [2, 5, 7])
  show_result(res)

  res = standard.shuffle_barriers("ABCDef", [4])
  show_result(res)

  res = standard.shuffle_barriers("bgywqa", [0, 1, 2, 4, 5])
  show_result(res)

  res = standard.shuffle_barriers("n", [0])
  show_result(res)
  res = standard.shuffle("hi")
  show_result(res)



def main():

  print("""Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
""")
  w = Wedding()
  while True:
    asktype=input().split()
    if asktype[0] == "quit":
      break;
    elif asktype[0] == "tests":
      standard_tests()
    elif asktype[0] == "s":
      guests = asktype[1]
      r = w.shuffle(guests)
      show_result(r);
    elif asktype[0] == "b":
      guests,nbar,bars = asktype[1],asktype[2],asktype[3:]
      r = w.shuffle_barriers(guests, [int(x) for x in bars])
      show_result(r)
    elif asktype[0] == "sp":
      guests,ind = asktype[1:]
      r = w.shuffle(guests);
      show_result(r, True, int(ind));
    elif asktype[0] == "bp":
      guests,nbar,bars,ind  = asktype[1],asktype[2],asktype[3:-1],asktype[-1]
      r = w.shuffle_barriers(guests, [int(x) for x in bars])
      show_result(r, True, int(ind))
    

if __name__ == '__main__':
  main()
