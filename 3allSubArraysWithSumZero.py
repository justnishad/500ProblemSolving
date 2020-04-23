'''Problem Statement'''
arr = input()
arr = arr.split()

subsets = []
sums2=0

for i in range(len(arr)):
  #to check wether whole array's sum is =0
  sums2=sums2+int(arr[i])
  temp=[]
  sums=0
  #normal logic to get all arrays with sum=0
  for j in range(i,len(arr)):
    sums=sums+int(arr[j])
    if(sums!=0):
      temp.append(arr[j])
    elif(sums==0):
      temp.append(arr[j])
      print(temp)

      subsets.append(temp)
      #temp.clear()
      break
if(sums2==0):
  subsets.append(arr)
print(subsets)

