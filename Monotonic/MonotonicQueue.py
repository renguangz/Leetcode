"""
https://leetcode.com/problems/sliding-window-maximum/submissions/1241855331/
與 monotonic stack 比起來，可以多檢查是否是過期無效的資料，從頭部移除
"""

def monotonicDequeue(nums, k):
    if not nums:
        return []
    res = [0] * (len(nums) - (k - 1))
    window = [] # 存 index, 並且 window 裡面的 index 換到 nums[index] 會是漸增
    for i in range(len(nums)):
        while window and window[0] < i - (k - 1): # 檢查 window 裡面存的是不是過期了，是的話就從頭部移除
            window.pop(0)

        while window and nums[i] > nums[window[-1]]: # 如果 current number 比最後面的數字大，就一直從尾部移除，直到比較大為止
            window.pop()

        window.append(i)

        if i >= k - 1:
            res[i - (k - 1)] = nums[window[0]]

    return res