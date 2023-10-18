class stack:
    def __init__(self):
        self.s = []
        self.minele = 0
        
    def push(self,a):
        if len(self.s)==0:
            self.s.append(a)
            self.minele = a 
            return 
        
        if a<self.minele:
            self.s.append(2*a - self.minele)
            self.minele = a
            
        else:
            self.s.append(a)
            
    def pop(self):
        ele = self.s.pop()
        if ele < self.minele:
            val = self.minele 
            self.minele = 2 * self.minele - ele
            return val 
            
        else:
            return ele
            
            
    def getMin(self):
        if len(self.s)==0:
            return -1
        return self.minele 
        
    def top(self):
        if len(self.s)==0:
            return -1
            
        ele = self.s[-1]
        if ele<self.minele:
            return self.minele
        else:
            return ele 
            
            
            
        
        
    
s = stack()
s.push(5)
print(s.getMin())
s.push(3)
print(s.getMin())
print(s.pop())
print(s.getMin())
print(s.pop())

s.push(8)
s.push(9)
print(s.top())
print(s.getMin())
s.push(2) 
print(s.top())
print(s.getMin())
print(s.pop())
print(s.getMin())
s.push(6)
print(s.getMin())
print(s.pop())
print(s.getMin())
