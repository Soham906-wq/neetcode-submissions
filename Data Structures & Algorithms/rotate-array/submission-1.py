class Solution:
    def rotate(self, nums, k):

        n = len(nums)
        k = k % n

        # Reverse the entire array
        left = 0
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Reverse the first k elements
        left = 0
        right = k - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Reverse the remaining elements
        left = k
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1