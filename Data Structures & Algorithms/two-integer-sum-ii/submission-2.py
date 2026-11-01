class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=0
        left=len(numbers)-1
        for i in range(0,len(numbers)):
            if numbers[right]+numbers[left]==target:
                return [right+1,left+1]
            elif numbers[right]+numbers[left]>target:
                left=left-1
            else:
                right=right+1