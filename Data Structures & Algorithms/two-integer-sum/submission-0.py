class Solution:
    def twoSum(self,nums,target):

        n = len(nums)

        for left in range(n):
            for right in range(left + 1,n):

                if nums[left] + nums[right] == target:
                    return [left,right]
        
        
        