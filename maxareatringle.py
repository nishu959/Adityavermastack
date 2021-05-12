
def MAH(arr):
  s = []
  v = []
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
  left = v
  s = []
  v = []
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
  right = v
  width = []
  for i in range(len(right)):
    width.append(right[i]-left[i]-1) 
  area=[]  
  for i in range(len(arr)):
    area.append(arr[i] * width[i]) 
  return max(area)


a = []
for i in range(int(input())):
  a.append(list(map(int,input().split())))
arr = []
for j in range(len(a[0])):
  arr.append(a[0][j])
mx = MAH(arr)
for i in range(1,len(a)):
  for j in range(0,len(a[0])):
    if a[i][j] == 0:
      arr[j] = 0
    else:
      arr[j]  = arr[j] + a[i][j]
  mx = max(mx, MAH(arr))
print(mx)