class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k in range(len(nums)):
            for l in range(k+1, len(nums)):
                if nums[k] + nums[l] == target:
                    return [k, l]
