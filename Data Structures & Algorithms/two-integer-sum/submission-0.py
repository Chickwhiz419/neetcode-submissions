class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idict = {}
        for i,num in enumerate(nums):
            if target - num in idict:
                return [idict[target-num],i]
            else:
                idict[num] = i

