

arr=[1,3,2,4,-1,9,5,10,6]       
stack = []
ans = []
n = len(arr)

for i in range(0, n):
    
    if len(stack)==0:
        ans.append(-1)
        
    else:
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop()
    
                
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
            
        
        
    stack.append(arr[i])
    
print(ans)
