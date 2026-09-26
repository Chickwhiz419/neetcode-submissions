class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        big = 0
        best = 0

        for num in nums:
            if num == 1:
                big += 1
                best = max(best,big)
            else:
                big = 0

        return best
                

        