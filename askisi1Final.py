import random as rand

sumsuccess=0
for k in range(0,1000):
  playersnumbs=[]
  for i in range(0,100):
    numbers=[]
    for j in range(0,5):
      number=rand.randrange(0,80)
      while number in numbers:
        number=rand.randrange(0,80)
      numbers.append(number)
    playersnumbs.append(numbers)

  success=0
  winnumbs=[]
  cond=False
  while cond==False:
    success=success+1
    winnum=rand.randrange(0,80)
    while winnum in winnumbs:
      winnum=rand.randrange(0,80)
    for j in range(0,100):
      if winnum in playersnumbs[j]:
        playersnumbs[j].remove(winnum)
    for j in range(0,100):
      if len(playersnumbs[j])==0:
        cond=True
  sumsuccess=sumsuccess+success

print("O mesos oros anaggelion einai  {}".format(sumsuccess/1000))
