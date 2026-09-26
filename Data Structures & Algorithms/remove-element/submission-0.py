class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       p,q= 0,0
       while p < len(nums):
        if nums[p] != val:
            nums[q] = nums[p]
            q += 1
            p += 1
        else:
            p += 1

       return q
        

    