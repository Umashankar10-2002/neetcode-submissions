class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highCount = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                count = 0
                
            else:
                count = count + 1

                if highCount < count :
                    highCount = count
            i = i + 1
        return highCount