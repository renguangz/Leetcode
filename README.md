# Leetcode sheet
## Python Tips
```python
list.sort(key=len) # sort by length
list.pop(0) # remove first element
dp = [0] * len(list) # one dimesion
dp = [[0] * len(list)] for _ in range(len(list)) # two dimesions
list.append() & list.pop(0) # time complexity O(n)
list.pop() # remove last element time complexity O(1)
```

### Longest Prefix Sum
```python
# 比對兩個陣列有幾組一樣的
arr1 = [0,2,1,1,0,2]
arr2 = [1,0,2]
# window - time complexity: O(n * m), n -> len(arr1), m -> len(arr2)
for i in range(len(arr1) - len(arr2) + 1):
    is_match = True
    for j in range(len(arr2)):
        if arr1[i + j] != arr2[j]:
            is_match = False
            break
    if is_match:
        result += 1

# Rabin karp - time complexity: O(n + m), n -> len(arr1), m -> len(arr2)
arr2_result = arr2[0]
for i in range(1, len(arr2)):
    arr2_result = arr2_result * 10 + arr2[i] # 下一個數字加進來的總和會是前面 * 10 加上當前數字
first_k_sum = arr1[0]
for i in range(1, len(arr2)):
    first_k_sum = first_k_sum * 10 + arr1[i]
current = first_k_sum
count = 0
if current == arr2_result: count += 1
mod_num = 10 ** (len(arr2) + 1) # 每次加入新的數字取 10^len(arr2)+1 餘數
for i in range(len(arr2), len(arr1)):
    current = current * 10 + arr1[i]
    current = current % mod_num # 取餘數就會是最新的的數字
    if current == arr2_result: count += 1 # hash 完畢之後，只要跟結果是一樣的就可以加一

# KMP - time complexity: O(n + m), n -> len(arr1), m -> len(arr2)
# 利用 DP 去計算前面看過的字，前後綴有幾個字是相同的，之後再不匹配的時候，直接跳過
# https://www.youtube.com/watch?v=af1oqpnH1vA&ab_channel=%E5%A5%87%E4%B9%90%E7%BC%96%E7%A8%8B%E5%AD%A6%E9%99%A2
def build_next(patt):
    next = [0]
    prefix_len = 0 # 當前陣列前後綴的長度
    i = 1
    while i < len(patt):
        if patt[prefix_len] == patt[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            prefix_len = next[prefix_len - 1]
            if prefix_len == 0:
                next.append(0)
                i += 1
    return next
def kmp_search(string, patt):
    next = build_next(patt)
    i, j = 0, 0
    while i < len(string):
        if string[i] == patt[j]: # 字符匹配，指針往後
            i += 1
            j += 1
        elif j > 0: # 字符不匹配，根據 next 跳過子串前面的一些字符
            j = next[j - 1]
        else: # 字串第一個字符就不匹配
            i += 1
        if j == len(patt): # 匹配成功
            return i - j
```

### Dynamic Programming
* `dp[i]` 跟 `dp[i - 1]` 的關係

```python
# Top Down: DFS + Memo, think about whats the relation between index i and i - 1
def dfs(args):
    if True: return 'basic value'
    # Do Something
    dp[result] = 'Some Result' # Do memo here
    return 'Some Result'

# Bottom Up: Caculate result from beginning
for i in 'something':
    dp[i] = 'some value'

```