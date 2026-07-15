class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            curr = nums[i]
            rem = target - curr
            if rem in numbers:
                return [numbers[rem], i]
            else:
                numbers[curr] = i
        