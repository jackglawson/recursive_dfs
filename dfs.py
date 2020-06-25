def dfs(n, edges):
    edges_by_vertex = dict([(i, []) for i in range(n)])
    for edge in edges:
        edges_by_vertex[edge[0]].append(edge[1])
        edges_by_vertex[edge[1]].append(edge[0])

    undiscovered = set(range(n))

    def search(v):
        print('Just discovered vertex {}.'.format(v))
        undiscovered.remove(v)
        for w in edges_by_vertex[v]:
            if w in undiscovered:
                search(w)

    while undiscovered:
        first_vertex = undiscovered.pop()
        undiscovered.add(first_vertex)
        search(first_vertex)


dfs(8, [[0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 6], [4, 5], ])
