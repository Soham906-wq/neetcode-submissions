class Solution:
    def isAnagram(self, s,t):
        if len(s)!= len(t):
            return False

        hash = {}

        for ch in s:
            if ch in hash:
                hash[ch]+= 1

            else:
                hash[ch] = 1

        for ch in t:
            if ch not in hash:
                return False

            hash[ch]-=1

            if hash[ch] < 0:
                return False


        return True 
            

        