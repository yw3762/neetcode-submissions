class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # building adjacency dict (each entry to a list for which )
        graph = defaultdict(list) 

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        itin = []

        st = ["JFK"]

        while st:
            airport = st[-1]

            if graph[airport]:
                st.append(graph[airport].pop())
            else:
                itin.append(st.pop())

        return itin[::-1]