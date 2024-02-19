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
    i, j = 0, 0 # i 是 string index, j 是 patt index
    while i < len(string):
        if string[i] == patt[j]:
            print('i', i, 'j', j)
            i += 1
            j += 1
        elif j > 0:
            print('elif j > 0:', j, next[j - 1], 'next', next)
            j = next[j - 1] # 透過 dp 生成的 next 得知 j 要往前移動到哪個位置開始匹配
        else:
            i += 1
        if j == len(patt):
            return i - j

# result = kmp_search(main, pattern)
# print('result', result)