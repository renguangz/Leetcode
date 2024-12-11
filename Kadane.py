"""
找 subarray 最大或是最小的總和
cur_sum 計算當前的 subarray 總和
- 每次比較 當前加上新的數字 (最大表示 subarray 從前面開始) & 0 (最大表示 subarray 設置為空) & 自己的數字 (最大表示 subarray 從自己開始)
"""
arr = [-14, -1, 31, 8, 6, 1, 9, -14, 8, -31]

cur_sum = 0
max_sum = 0
for i in range(len(arr)):
    cur = arr[i]
    temp = cur_sum + cur
    max_sum = max(max_sum, temp)
    cur_sum = max(0, temp, cur)
print('答案：', max_sum)