class Solution:
    def leftSmaller(self, n, a):
        # code here
        
        stack = []
        ans = []
        
        for i in range(n):
            
            if len(stack)==0:
                ans.append(-1)
                
            else:
                
                while len(stack)>0 and stack[-1] >=a[i]:
                    stack.pop()
                    
                if len(stack)==0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                    
            stack.append(a[i])
                    
        return ans
