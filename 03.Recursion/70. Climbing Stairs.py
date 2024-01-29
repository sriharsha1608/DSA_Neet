class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        for i in range(0,n):
            a,b=b,a+b
        return b
            
