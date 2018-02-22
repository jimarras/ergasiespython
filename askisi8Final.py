import random as rand

numbers=[]
for i in range(0,30):
    randomnumb=rand.randrange(-30,30)
    while randomnumb in numbers:
      randomnumb=rand.randrange(-30,30) 
    numbers.append(randomnumb)
numbers.sort()

i=0
while(numbers[i]<0):
    i=i+1
thesi0=i

Ntriadwn=0
for i in range(0,28):
  for j in range(i+1,30):
    if (numbers[i]+numbers[j]<=0):
      if j<thesi0:
        for k in range(thesi0,30):
          if (numbers[i]+numbers[j]+numbers[k]==0):
            Ntriadwn=Ntriadwn+1
            print('{}) {},{},{} \n'.format(Ntriadwn,numbers[i],numbers[j],numbers[k]))
      else:
        for k in range(j+1,30):
          if (numbers[i]+numbers[j]+numbers[k]==0):
            Ntriadwn=Ntriadwn+1
            print('{}) {},{},{} \n'.format(Ntriadwn,numbers[i],numbers[j],numbers[k]))
    else:
      if j<thesi0:
        for k in range(j+1,thesi0):
          if (numbers[i]+numbers[j]+numbers[k]==0):
            Ntriadwn=Ntriadwn+1
            print('{}) {},{},{} \n'.format(Ntriadwn,numbers[i],numbers[j],numbers[k]))
print(Ntriadwn)