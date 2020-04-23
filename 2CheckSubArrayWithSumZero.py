arr = input()
arr = arr.split()
sums = 0
set = []
x = 0
set.append(sums)
for i in range(len(arr)):
    sums = sums + int(arr[i])
    if (sums in set):
        x = 1
        break
    else:
        set.append(sums)

if (x == 1):
    print('exists')
else:
    print('not exists')
'''
Explaination:
We create a set which stores sum of the elemnents at each iteration.
First element of that set is 0.
It is kept in order to find wether sum at any stage ever gets to zero or not.
Problem-Statement:https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/

'''
