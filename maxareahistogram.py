def solve1(arr, s, v):
  for i in range(0,len(arr),1):
    if len(s)==0:
      v.append(-1)
    elif (len(s)>0 and s[-1][0]<arr[i]):
      v.append(s[-1][1])
    elif (len(s)>0 and s[-1][0]>=arr[i]):
      while(len(s)>0 and s[-1][0]>=arr[i]):
        s.pop()
      if len(s)==0:
        v.append(-1)
      else:
        v.append(s[-1][1])
    s.append([arr[i], i])
  return v


def solve2(arr, s, v):
  for i in range(len(arr)-1,-1,-1):
    if len(s)==0:
      v.append(len(arr))
    elif (len(s)>0 and s[-1][0]<arr[i]):
      v.append(s[-1][1])
    elif (len(s)>0 and s[-1][0]>=arr[i]):
      while(len(s)>0 and s[-1][0]>=arr[i]):
        s.pop()
      if len(s)==0:
        v.append(len(arr))
      else:
        v.append(s[-1][1])
    s.append([arr[i], i])
  v.reverse()
  return v
     
arr = list(map(int, input().split()))
v = []
q =solve1(arr,[],v)
v = []
p = solve2(arr, [], v)
right = p
left = q
width = []
#NSR and NSL
print(right)
print(left)
for i in range(len(p)):
  width.append(right[i]-left[i]-1) 
#width
print(width)
area=[]  
  
for i in range(len(arr)):
  area.append(arr[i] * width[i]) 
#area
print(area)  
#maxarea
print(max(area)) 
  
