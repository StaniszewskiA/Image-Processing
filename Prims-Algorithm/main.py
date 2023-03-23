import heapq

mst = []
usedVertices = set()
with open("PrimMST_input0..txt") as f:
    numVertices = int(f.readline())
    graph = [[] for _ in range(numVertices)]
    for line in f.readlines():
        u, v, weight = map(int, line.split())
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    heap = []
    heapq.heappush(heap, (0,0))

    parent = [None] * numVertices

    while heap:
        weight, vertex = heapq.heappop(heap)
        if vertex in usedVertices:
            continue

        usedVertices.add(vertex)
        for edge in graph[vertex]:
            if edge[1] not in usedVertices:
                heapq.heappush(heap,edge)

                if parent[edge[1]] is None or edge[0] < graph[edge[1]][parent[edge[1]]][0]:
                    parent[edge[1]] = len(mst)

        if weight > 0:
            mst.append((vertex, parent[vertex], weight))

print(mst)