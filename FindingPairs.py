''' ProblemStatement : https://www.techiedelight.com/find-pair-with-given-sum-array/ '''
arr=input()
arr=arr.split()
s=int(input())
ival=[]
jval=[]
def FindPair(arr,s):
  for i in range(len(arr)):
        x=abs(int(arr[i])-s)
        j=0
        if str(x) in arr:
          j=arr.index(str(x))
          if (j!=i) and (i not in jval) and (j not in ival):
            print(i,j)
            ival.append(i)
            jval.append(j)

FindPair(arr,s)