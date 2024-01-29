class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[0,0,0]
        for i in nums:
            a[i]+=1
        k=0
        for i in range(len(a)):
            for j in range(a[i]):
                nums[k]=i
                k+=1