class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for i in s:
            if i not in count1:
                count1[i] = 1
            else:
                count1[i] = count1[i] + 1
        for j in t:
            if j not in count2:
                count2[j] = 1
            else:
                count2[j] = count2[j] + 1
        if count1 == count2:
            return True
        return False