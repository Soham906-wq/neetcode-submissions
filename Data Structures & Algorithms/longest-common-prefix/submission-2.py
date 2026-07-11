class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""

        prefix = ""

        # Traverse each character of the first string
        for i in range(len(strs[0])):

            ch = strs[0][i]

            # Compare this character with all other strings
            for j in range(1, len(strs)):

                # If index goes out of range or characters don't match
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return prefix

            # Character matched in every string
            prefix += ch

        return prefix