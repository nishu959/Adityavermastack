#User function Template for python3


class Solution:
    
    def maxArea(self,M, n, m):
        # code here
    
        def MAH(heights):
            stack = []
            n = len(heights)
            NSL = [-1]*n
            
            for i in range(n):
                
                while len(stack)>0 and stack[-1][0]>=heights[i]:
                    stack.pop()

                if len(stack)==0:
                    NSL[i]=-1
                else:
                    NSL[i] = stack[-1][1]
    
                stack.append([heights[i], i])
    
            stack=[]
            NSR=[n]*n
            n = len(heights)
    
            for i in range(n-1, -1, -1):
                
                while len(stack)>0 and stack[-1][0]>=heights[i]:
                    stack.pop()
                if len(stack)==0:
                    NSR[i]=n
                else:
                    NSR[i]=stack[-1][1]
    
                stack.append([heights[i],i])
    
            
        
    
            area = 0
            for i in range(n):
                area = max(area , (NSR[i]-NSL[i]-1)*heights[i])
            return area
            
        
        arr= M[0]
        mx= MAH(arr)
        
        for i in range(1,n):
            
            for j in range(m):
                
                if M[i][j]==0:
                
                    arr[j]=0
                else:
                    arr[j]+=1
                    
            
            mx = max(mx, MAH(arr))
        
        return mx
                


        
        
        
