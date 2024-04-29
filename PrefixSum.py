"""
3, 8, 4, 7, 2, 3, 5,10, 9

3,11,15,18,20,23,28,38,47

跑一個迴圈把數字加起來，接下來如果要求 i ~ j 總和
if j == 0: prefixSum[i]
else: prefixSum[i] - prefixSum[j - 1]
"""

# 把每個數字加起來
def prefixSum(nums):
    for i in range(1, len(nums)):
        cur = nums[i]
        prev = nums[i - 1]
        cur += prev
    return nums

def sumRange(nums, left, right):
    res = prefixSum(nums)
    if left == 0:
        return res[right]
    else:
        return res[right] - res[left - 1]