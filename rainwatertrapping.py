a = list(map(int, input().split()))
mxl = [None]*len(a)
mxl[0] = a[0]
for i in range(1,len(a)):
  mxl[i] = max(a[i],mxl[i-1])
  
mxr = [None]*len(a)
mxr[len(a)-1] = a[len(a)-1]
for i in range(len(a)-2,-1,-1):
  mxr[i] = max(a[i], mxr[i+1])

width = [None]*len(a)
for i in range(len(a)):
  width[i] = min(mxl[i], mxr[i]) - a[i]
 
print(sum(width)) 