class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        NSL = []
        n = len(heights)
        for i in range(n):
            
            while len(stack)>0 and stack[-1][0]>=heights[i]:
                stack.pop()

            if len(stack)==0:
                NSL.append(-1)
            else:
                NSL.append(stack[-1][1])

            stack.append([heights[i], i])

        stack=[]
        NSR=[]
        n = len(heights)

        for i in range(n-1, -1, -1):
            
            while len(stack)>0 and stack[-1][0]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                NSR.append(n)
            else:
                NSR.append(stack[-1][1])

            stack.append([heights[i],i])

        # print(NSL)
        NSR= NSR[::-1]

        area = -sys.maxsize
        for i in range(n):
            area = max(area , (NSR[i]-NSL[i]-1)*heights[i])
        return area
