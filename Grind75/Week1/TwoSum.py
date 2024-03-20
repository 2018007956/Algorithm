class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, x in enumerate(nums):
            if x > target:
                pass

            if target-x in nums:
                tmp = [i for i,v in enumerate(nums) if v==target-x]
                if tmp[-1] != idx:
                    return [idx, tmp[-1]]