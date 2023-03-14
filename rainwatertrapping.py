a = list(map(int, input().split()))
mxl = [None]*len(a)
mxl[0] = a[0]
for i in range(1,len(a)):
  mxl[i] = max(a[i],mxl[i-1])
  
mxr = [None]*len(a)
mxr[len(a)-1] = a[len(a)-1]
for i in range(len(a)-2,-1,-1):
  mxr[i] = max(a[i], mxr[i+1])

width = [None]*len(a)
for i in range(len(a)):
  width[i] = min(mxl[i], mxr[i]) - a[i]
 
print(sum(width)) 



class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        leftmax = 0
        rightmax=0
        res=0

        while l<=r:
            if height[l] <= height[r]:
                
                if height[l]>=leftmax:
                    leftmax = max(leftmax, height[l])
                else:
                    res += leftmax-height[l]

                l += 1

            else:

                if height[r]>=rightmax:
                    rightmax = max(rightmax , height[r])
                else:
                    res += rightmax-height[r]

                r -= 1

        return res
