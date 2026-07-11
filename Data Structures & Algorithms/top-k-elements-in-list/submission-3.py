class Solution:
    def topKFrequent(self, nums, k):

        count = {}

        # Step 1: Count frequencies
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Step 2: Create buckets
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into buckets
        for num, c in count.items():
            freq[c].append(num)

        # Step 4: Collect answer
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result