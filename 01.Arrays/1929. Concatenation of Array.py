class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for j in nums:
                ans.append(j)

        return ans
        

########Other way######

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums+nums
        return ans

########Other way######

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2*len(nums)):
            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i-len(nums)])
        
        return ans