class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if x > total: return -1
        if x == total: return len(nums)

        nums.append(0)
        ops, left, right, length = 100000, 0, 0, len(nums)
        maxi = ops
        while right < length:
            if total > x:
                total -= nums[right]
                right += 1
            elif total < x:
                total += nums[left]
                left += 1
            else:
                ops = min(ops, length + left - right - 1)
                total = total + nums[left] - nums[right]
                left += 1
                right += 1
        return ops if ops != maxi else -1
