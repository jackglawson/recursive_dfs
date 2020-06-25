# Recursive depth first search

Given a list of all edges of a graph with vertices 1 to n, this algorithm will explore every vertex, depth first.
Useful when exploring a small graph (depth < 300) as this algorithm is simpler and requires less space than the non-recursive dfs.
Vertices are explored in lexicographic order.

Warning: will hit the python recursion limit if the graph is too large.