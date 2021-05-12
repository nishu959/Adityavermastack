s = []
ss = []

def push( a):
  s.append(a)
  if len(ss)==0 or a<=ss[-1]:
    ss.append(a) 
  print("pushed")
  return
  

def pop():
  if len(s)==0:
    return -1
  ans = s.pop()
  if ans ==ss[-1]:
    ss.pop() 
  return ans
  
    
def getmin():
  if len(s)==0:
    return -1
  return ss[-1]
  
 

