cond=True
while cond==True:
  try:
    num=int(input("Give integer: "))
    cond=False
  except ValueError:
    print("Please an integer")

diairetis=1
psifia=0
while num%diairetis!=num:
  diairetis=10*diairetis
  psifia=psifia+1
numb=[]
for x in str(num):
  numb.append(int(x))
s=0
for i in numb:
  s=s+i
deikths=0
for i in range(0,psifia):
  deikths=deikths+pow(10,i)
mini=s//psifia

j=9
while j>mini:
  katw=j*pow(10,psifia-1)
  anw=j*deikths+1
  for i in range(katw,anw):
    cond=True
    numbeo=[]
    for k in str(i):
      numbeo.append(k)
    for k in range(0,psifia-1):
      if numbeo[k]<numbeo[k+1]:
        cond=False
    if cond==True:
      summ=0
      for k in numbeo:
        summ=summ+int(k)
    if cond==True and summ==s:
      print(i)
  j=j-1