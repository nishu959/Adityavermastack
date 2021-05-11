def solve(arr, s, v):
  for i in range(len(arr)-1,-1,-1):
    if len(s)==0:
      v.append(-1)
    elif (len(s)>0 and s[-1]<arr[i]):
      v.append(s[-1])
    elif (len(s)>0 and s[-1]>arr[i]):
      while(len(s)>0 and s[-1]>=arr[i]):
        s.pop()
      if len(s)==0:
        v.append(-1)
      else:
        v.append(s[-1])
    s.append(arr[i])
  v.reverse()
  return v
 
arr = list(map(int, input().split()))
v = []

print(solve(arr,[],v))