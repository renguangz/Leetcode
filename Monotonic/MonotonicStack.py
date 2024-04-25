"""
https://zhuanlan.zhihu.com/p/346354943
"""
# 漸增
def monotonicIncreasing(nums):
    stack, res = [], []
    for num in nums:
        # while stack is not empty and the top of stack is more than the element
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)

    # Construct the res array from stack
    while stack:
        res.insert(0, stack.pop())

    return res

# @example
nums = [3, 1, 4, 1, 5, 9, 2, 6]
res = monotonicIncreasing(nums)
print(res)
