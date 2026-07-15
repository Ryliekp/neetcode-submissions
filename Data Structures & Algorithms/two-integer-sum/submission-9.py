class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, n in enumerate(nums):
            rem = target - n
            if rem in numbers:
                return [numbers[rem], i]
            else:
                numbers[n] = i
        