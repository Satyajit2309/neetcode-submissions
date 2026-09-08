class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        result = combSum(nums , target , [] , 0 , [] )

        return result


def combSum(nums , target , result , ind , curr):
    if ind == len(nums):
        return result
    
    if target < 0:
        return result 

    if target == 0:
        result.append(curr.copy())
        return result 

    if nums[ind] <= target:
        curr.append(nums[ind])
        combSum(nums, target- nums[ind] , result , ind , curr)
    
        curr.pop()
    combSum(nums , target , result , ind+1 , curr)

    return result 