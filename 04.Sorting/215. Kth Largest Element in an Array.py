class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        c=len(nums)-k
        return nums[c]



### tried merge approach not worked

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # nums.sort()
#         # c=len(nums)-k
#         # return nums[c]
#         k=len(nums)-k

#         def quick(l,r):
#             p,pi=l,nums[r]
#             for i in range(l,r):
#                 if nums[i]<=pi:
#                     nums[p],nums[i]=nums[i],nums[p]
#                     p+=1
#             nums[p],nums[r]=nums[r],nums[p]

#             if p>k:
#                 return quick(l,p-1)
#             elif p<k:
#                 return quick(p+1,r)
#             else:
#                 return nums[p]
#         return quick(0,len(nums)-1)
