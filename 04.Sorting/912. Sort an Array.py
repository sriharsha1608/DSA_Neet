## Merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l,m,r):
            le,ri=arr[l:m+1],arr[m+1:r+1]
            i,j,k=l,0,0
            while j<len(le) and k<len(ri):
                if le[j]<=ri[k]:
                    arr[i]=le[j]
                    j+=1
                else:
                    arr[i]=ri[k]
                    k+=1
                i+=1
            while j <len(le):
                arr[i]=le[j]
                i+=1
                j+=1
            while k <len(ri):
                arr[i]=ri[k]
                i+=1
                k+=1
        

        def div(arr,l,r):
            if l==r:
                return arr
            
            m=(l+r)//2
            div(arr,l,m)
            div(arr,m+1,r)
            merge(arr,l,m,r)
            return arr
        
        return div(nums,0,len(nums)-1)


## Insertion sort code ##

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         for i in range(1,len(nums)):
#             j=i-1
#             while j>=0 and nums[j+1]<nums[j]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#                 j-=1
        
#         return nums