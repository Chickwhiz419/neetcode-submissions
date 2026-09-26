class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big = -1
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            arr[i] = big
            big = max(curr,big)
        return arr
            
            
        