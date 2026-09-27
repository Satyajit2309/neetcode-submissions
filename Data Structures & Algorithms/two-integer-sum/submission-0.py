class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}

        for i in range(len(nums)):
            numset[nums[i]] = i
        

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numset and numset[diff] != i:
                return [i , numset[diff]]
        
        return []