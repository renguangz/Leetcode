import heapq
"""
概念：從初始點開始標記初始點並尋找可以到的點，紀錄最短路徑以及最短路徑的前一個點是哪裡來的，一輪找完之後，從 PQ 找最小的路徑標記，並尋找所有可以到的點

1. 初始值為無限大的 Array，用來記錄 Shortest dist from start
2. 一個 map，紀錄每個點的 prev 是誰
3. 一個 MinHeap 紀錄當前最小的路徑是誰，作為下一個計算的目標

* mark all vertices as unvisited initially
* mask all nodes with infinite distance initially except source node
* repeat the following for (v - 1) times:
    (1) pick the min value node which is unvisited
    (2) mark the node as visited
    (3) udpate all adjacent vertices
        - if cost[u] + weight(uv) < cost[v] (u -> v, 意即從 u 加上 u 到 v weight 比到 v 的距離小的話就 update)
"""


"""
shortest path by bfs (dijkstra)
* adj Map 紀錄所有點可以到哪些點，以及分別需要多少 weight
* min heap 紀錄可以到達的點的距離
* shortest 紀錄從初始點到達每個點需要多遠的距離，因為是 minHeap，所以會出現的點都是最小的距離，不需要再判斷
"""

def dijkstra(n, edges, src):
    adj = {}
    for i in range(n):
        adj[i] = []

    for source, dist, weight in edges:
        adj[source].append((dist, weight)) # 表示可以到達的點以及 weight

    shortest = {} # Map vertex -> dist of shortest path
    prev = {} # Previous node in the shortest path
    minHeap = [[0, src]]
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        # 因為是 minHeap，比較小的會先被叫到並且存入 shortest，因此這邊可以直接判斷是不是有被存過，存過則跳過，進入下一個 while loop
        if n1 in shortest:
            continue
        shortest[n1] = w1

        # 從當前 n1 點，透過 adj Map 去找可以到哪些其他點，並存到 minHeap 中
        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                prev[n1] = n2 # update previous node
                heapq.heappush(minHeap, [w1 + w2, n2])

    return shortest, prev

    


# @example
# idx 0 & 1 -> 各代表一個點且無方向性, idx 2 -> 距離
edges = [[0,1,4],[0,7,8],[1,7,11],[1,2,8],[2,8,2],[7,8,7],[7,6,1],[8,6,6],[6,5,2],[2,5,4],[2,3,7],[3,4,9],[5,4,10]]
n = 9
src = 0
dist = 4
res, prev = dijkstra(n, edges, src)
print(res[dist]) # should be 21
print(prev) # 會紀錄每個點下一個會去到哪裡，構成最短路徑