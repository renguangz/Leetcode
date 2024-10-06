"""
對多個數字做分組，例如 1,2 同組，接下來可以把 1,6 or 2,6 分在同一組，find 的時候可以依照 parent 分組快速找到所有同組的 item (nlogn)

EXAMPLE: [1,2,3,4,5,6]
* 使用另一個 List (parent) 紀錄
parent = [1,2,3,4,5,6]
* 透過 union function 把 parent 資料合併在一起
parent =  [1 1 3 4 5 1]
example = [1 2 3 4 5 6]
* 透過 find 在 parent 尋找合併再一起的資料
find(6) = find(2) = find(1)
find(3) != find(4) != find(5) != find(1)

https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
"""
parent = []  # 初始化陣列等於原始陣列


def find(x: int):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x: int, y: int):
    if find(x) != find(y):
        parent[parent[y]] = parent[x]


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        """
        union by size: 當要合併兩個子集，會希望是大的合併小的，會讓樹的高度比較小
        union by rank: 根據 rank 大小決定合併，大的合併小的，合併別人的子集其 rank 會往上升
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_x]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
