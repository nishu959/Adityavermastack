class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        stack = []
        ans = []
        n = len(a)
        
        for i in range(0, n):
            
            if len(stack)==0:
                ans.append(-1)
                
            else:
                while len(stack)>0 and stack[-1][0]<=a[i]:
                    stack.pop()
            
                        
                if len(stack)==0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1][1])
                    
                
                
            stack.append([a[i], i])
            
        
        
        for i in range(len(ans)):
            ans[i] = i - ans[i]
            
        
        return ans
