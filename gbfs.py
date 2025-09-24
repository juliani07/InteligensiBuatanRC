import heapq

graph = {
    'Cilegon': {'Tangerang': 90},
    'Tangerang': {'Jakarta': 20},
    'Jakarta': {'Bekasi': 25},
    'Bekasi': {'Subang': 120},
    'Subang': {'Bandung': 60},
    'Bandung': {'Tasikmalaya': 110},
    'Tasikmalaya': {'Cilacap': 140},
    'Cilacap': {'Purwokerto': 40},
    'Purwokerto': {'Kebumen': 60},
    'Kebumen': {'Yogyakarta': 100},
    'Yogyakarta': {'Surakarta': 65},
    'Surakarta': {'Ngawi': 90},
    'Ngawi': {'Nganjuk': 70},
    'Nganjuk': {'Sidoarjo': 90},
    'Sidoarjo': {'Probolinggo': 80},
    'Probolinggo': {'Situbondo': 100},
    'Situbondo': {'Banyuwangi': 90}
}

heuristic = {
    'Cilegon': 950, 'Tangerang': 882, 'Jakarta': 861, 'Bekasi': 840,
    'Subang': 750, 'Bandung': 780, 'Tasikmalaya': 684, 'Cilacap': 640,
    'Purwokerto': 571, 'Kebumen': 530, 'Yogyakarta': 490, 'Surakarta': 450,
    'Ngawi': 380, 'Nganjuk': 320, 'Sidoarjo': 280, 'Probolinggo': 200,
    'Situbondo': 120, 'Banyuwangi': 0
}

def gbfs(start, goal):
    frontier = [(heuristic[start], start, [start], 0)]  # (h(n), node, path, cost)
    visited = set()

    while frontier:
        h, node, path, cost = heapq.heappop(frontier)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, distance in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(frontier, (heuristic[neighbor], neighbor, path + [neighbor], cost + distance))

    return None, None

start, goal = 'Cilegon', 'Banyuwangi'
path, cost = gbfs(start, goal)

print("=== Greedy Best First Search (GBFS) ===")
if path:
    print("Jalur:", " -> ".join(path))
    print("Total jarak (tidak selalu optimal):", cost, "km")
else:
    print("Jalur tidak ditemukan!")
