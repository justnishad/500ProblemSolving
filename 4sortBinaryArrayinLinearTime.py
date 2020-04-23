'''Problem Statement:https://www.techiedelight.com/sort-binary-array-linear-time/ '''
arr = input()
arr = arr.split()

zero=(arr.count(str(0)))
one=(arr.count(str(1)))

a1=[]
a2=[]
for i in range(max(zero,one)):
  if(i<zero):
    a1.append(0)
  if(i<one):
    a2.append(1)

a1.extend(a2)
print(a1)

