s = []
minele= 100
def push(a):
  global minele
  if len(s)==0:
    s.append(a)
    minele = a
    return
    
  if a>= minele:
    s.append(a)
  elif a<minele:
    s.append(2*a-minele)
    minele = a
  return
  


def pop():
  global minele
  if len(s)==0:
    return
  else:
    if s[-1]>=minele:
      s.pop()
    elif s[-1]<minele:
      minele = 2*minele - s[-1]
      s.pop()
  return
  
  
def getmin():
  if len(s)== 0:
    return -1
  return minele
  
def top():
  if len(s)==0:
    return -1
  if s[-1]>= minele:
    return s[-1]
  elif s[-1]<minele:
    return minele
      
      
    
#for checking the above program optional
push(5)
push(7)
print(s)
print(top())
print(getmin())
pop()
print(s)
print(getmin())
push(2)
print(s)
print(getmin())
push(8)
print(s)

print(getmin())
print(top())
pop()
pop()
print(getmin())
print(s)
print(top())