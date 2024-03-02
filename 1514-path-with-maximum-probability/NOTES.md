# dijkstra

# Floyd Warshall
dijkstra complexity = O(nmlogn) but somtimes m can be close to n^2 so it can be n^3logn.
In this case, using Floyd Warshall algorithm is more efficient:
f(k, i, j) = min(f(k-1, i, j), f(k-1, i, k) + f(k-1, k, j))​
