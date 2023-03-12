
class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack = []
        ans = []
        
        for i in range(n-1, -1, -1):
            
            if len(stack)==0:
                ans.append(-1)
                
            else:
                
                while len(stack)>0 and stack[-1]>= arr[i]:
                    stack.pop()
                    
                if len(stack)==0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                    
            stack.append(arr[i])
            
        
        return ans[::-1]
