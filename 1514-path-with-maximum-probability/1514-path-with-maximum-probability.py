from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        max_heap = [(-1, start_node)]

        new_edges = defaultdict(list)
        for i in range(len(edges)):
            new_edges[edges[i][0]].append([edges[i][1], succProb[i]])
            new_edges[edges[i][1]].append([edges[i][0], succProb[i]])

        visited = set()
        while max_heap:
            cur_prob, node = heapq.heappop(max_heap)
            if node == end_node:
                return -1 * cur_prob
            visited.add(node)
            for next_node_info in new_edges[node]:
                if next_node_info[0] in visited:
                    continue
                heapq.heappush(max_heap, [cur_prob*next_node_info[1], next_node_info[0]])
        

        return 0