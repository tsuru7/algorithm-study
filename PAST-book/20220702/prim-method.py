from heapq import heappush, heappop
def prim_method(graph):
    n = len(graph)
    marked = [False for _ in range(n)]
    marked_count = 0

    marked[0] = True
    marked_count = 1

    heap = []
    for v, c in graph[0]:
        heappush(heap, (c, v))

    sum = 0
    while marked_count < n:
        c, u = heappop(heap)
        if marked[u]:
            continue
        marked[u] = True
        marked_count += 1
        sum += c
        for v, c in graph[u]:
            if marked[v]:
                continue
            heappush(heap, (c, v))
    return sum

