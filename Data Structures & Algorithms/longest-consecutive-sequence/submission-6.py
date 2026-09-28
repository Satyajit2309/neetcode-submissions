# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # numbers = set(sorted(nums))
#         nums.sort()
#         if not nums:
#             return 0

#         curr = 1
#         best = 1

#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 continue
#             elif nums[i] == nums[i-1] + 1:
#                 curr += 1
#             else:
#                 curr = 1

#             best = max(best, curr)

#         return best


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest