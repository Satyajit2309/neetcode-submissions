class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numbers = set(sorted(nums))
        nums.sort()
        if not nums:
            return 0

        curr = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                curr = 1

            best = max(best, curr)

        return best