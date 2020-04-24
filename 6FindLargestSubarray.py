#Problem Statement:https://www.techiedelight.com/find-largest-sub-array-formed-by-consecutive-integers/
arr = input()
arr = arr.split()
temp=[]
final=[]
for i in range(len(arr)):

  for j in range(i,len(arr)):
    if(arr[j] not in temp):
      temp.append(arr[j])
    else:
      if(len(temp)>len(final)):
        final=[]
        final.extend(temp)
      temp.clear()
      break
print(final)
#2 0 2 1 4 3 1 0
