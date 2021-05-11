def solve(arr, s, v):
  for i in range(0,len(arr),1):
    if len(s)==0:
      v.append(-1)
    elif (len(s)>0 and s[-1][0]>arr[i]):
      v.append(s[-1][1])
    elif (len(s)>0 and s[-1][0]<=arr[i]):
      while(len(s)>0 and s[-1][0]<=arr[i]):
        s.pop()
      if len(s)==0:
        v.append(-1)
      else:
        v.append(s[-1][1])
    s.append([arr[i], i])
  return v
 
arr = list(map(int, input().split()))
v = []
p =solve(arr,[],v)
s = []
for i in range(len(p)):
  s.append(i-p[i])
print(s)