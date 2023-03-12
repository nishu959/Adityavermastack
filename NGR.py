class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack = []
        ans = []
        
        
        for i in range(n-1, -1, -1):
            
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
            
        # print(ans)
        return ans[::-1]
