"""
以 Binary Tree 做 Priority Queue
"""

class Node:
    def __init__(self, val, priority) -> None:
        self.val = val
        self.priority = priority

class PriorityQueue:
    def __init__(self) -> None:
        self.values = []

    def enqueue(self, val, priority):
        newNode = Node(val, priority)
        # 把值放在最後一個然後做 bubble up
        self.values.append(newNode)
        self.bubbleUp()

    def dequeue(self):
        min = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            # 把最後一個拿掉取代 root，並且做 sinkDown 再次排序
            self.values[0] = end
            self.sink_down()
        # 回傳 root 值 
        return min

    def bubble_up(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]
            if element.priority >= parent.priority:
                break
            # 子節點跟父節點 swap
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx

    def sink_down(self):
        idx = 0
        length = len(self.values)
        # root 的值
        element = self.values[0]
        while True:
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            left = right = swap = None
            if leftChildIdx < length: # smaller than array self.values length
                left = self.values[leftChildIdx]
                if left.priority < element.priority:
                    # 因為是 min heap，如果左邊的比 root 小，那左邊應該至少就要跟 root swap
                    swap = leftChildIdx
            if rightChildIdx < length: # smaller than array self.values length
                right = self.values[rightChildIdx]
                # 如果右邊比 root 小且 swap 是 None，表示左邊比 root 大
                # 如果右邊比 root 小但 swap 不是 None，表示左邊也比 root 小，因此要去判斷左邊還是右邊是更小值，往小的那邊 swap
                if (swap is None and right.priority < element.priority) or (swap is not None and right.priority < left.priority):
                    swap = rightChildIdx
            # 如果 swap is None，表示 root 比左右都要小
            if swap is None:
                break
            # 這邊對剛剛紀錄的 swap index & root 做對調
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


# @example
