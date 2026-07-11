class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans


# --------- Examples ---------

solution = Solution()

# Example 1
input_nums = [1, 4, 1, 2]
print(solution.getConcatenation(input_nums))
# Output: [1, 4, 1, 2, 1, 4, 1, 2]

# Example 2
input_nums = [22, 21, 20, 1]
print(solution.getConcatenation(input_nums))
# Output: [22, 21, 20, 1, 22, 21, 20, 1]
