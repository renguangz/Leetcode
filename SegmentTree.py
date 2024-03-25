"""
用途：求區間中最大值、最小值、總和
Max tree, Min tree, Sum tree -> 複雜度 , build time: O(n), 查找: O(logN)

題目範例:
https://leetcode.com/problems/most-frequent-ids/
"""
class SegmentTree:
    def __init__(self,nums):
        self.nums = nums
        self.arr = [0]*(max(self.nums)+1)
        self.n = len(self.arr)
        self.tree = {}
        self.build(0, 0, self.n - 1)

    def build(self,ind,left,right):
        if left == right:
            self.tree[ind] = self.arr[left]
            return
        mid = (left+right)//2
        self.build(2*ind+1,left,mid)
        self.build(2*ind+2,mid+1,right)
        # change here if not going to use max tree
        self.tree[ind] = max(self.tree[2*ind+1], self.tree[2*ind+2])
    
    def update(self, ind, left, right, node, val):
        if left == right:
            self.tree[ind] += val
            return
        mid = (left+right)//2
        if node<=mid:
            self.update(2*ind+1,left,mid,node,val)
        else:
            self.update(2*ind+2, mid+1,right,node,val)
        # change here if not going to use max tree
        self.tree[ind] = max(self.tree[2*ind+1], self.tree[2*ind+2])
    
    def query(self,ind):
        return self.tree[ind]