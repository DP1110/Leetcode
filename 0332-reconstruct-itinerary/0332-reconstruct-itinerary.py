from collections import defaultdict
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for a, b in tickets:
            heapq.heappush(graph[a], b)

        route = []
        def dfs(node):
            while graph[node]:
                nxt = heapq.heappop(graph[node])
                dfs(nxt)
            route.append(node)

        dfs("JFK")
        return route[::-1]