''' Problem Statement:https://www.techiedelight.com/find-duplicate-element-limited-range-array/ '''
arr = input()
arr = arr.split()
temp=[]
for i in arr:
  if i not in temp:
    temp.append(i)
  else:
    print("Duplicate is "+i)
