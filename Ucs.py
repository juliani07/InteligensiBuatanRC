import heapq

graph = {
    'Cilegon': {'Tangerang': 81},
    'Tangerang': {'Jakarta': 29},
    'Jakarta': {'Bekasi': 22, 'Depok': 25},
    'Bekasi': {'Depok': 41, 'Subang': 95, 'Indramayu': 185},
    'Depok': {'Bogor': 44},
    'Bogor': {'Sukabumi': 57},
    'Sukabumi': {'Bandung': 93},
    'Bandung': {'Tasikmalaya': 83, 'Cirebon': 106},
    'subang' : {'Cirebon' :103},
    'Indramayu':{'Cirebon' :56},
    'Tasikmalaya': {'Cilacap': 96, 'Purwakerto': 113},
    'Cirebon' :{'tegal':71},
    'Cilacap': {'Kebumen': 70, 'Purwokerto': 42},
    'Purwokerto': {'Kebumen': 51, 'Magelang': 107, 'Tegal':65},
    'tegal' :{'Purwokerto':65, 'Pekalongan' :70},
    'Kebumen': {'Yogyakarta': 81},
    'Yogyakarta': {'Pacitan': 107, 'Surakarta': 75, 'Magelang': 40},
    'pacitan': {'Trenggelak': 106},
    'Trenggelak': {'Kepanjen':114, 'Nganjuk':108},
    'Kepanjen': {'Lumajang':116},
    'Pekalongan': {'Semarang': 83},
    'Magelang': {'Ambarawa': 35, 'Yogyakarta' :40},
    'Ambarawa': {'Surakarta': 70, 'Semarang': 37},
    'Semarang': {'Kudus': 60},
    'Surakarta': {'Ngawi': 83},
    'Kudus': {'Rembang': 62},
    'Rembang': {'Bojonegoro': 103, 'Tuban': 93},
    'Tuban': {'Surabaya': 95},
    'Surabaya': {'Bojonegoro': 111, 'Sidoarjo': 35},
    'Sidoarjo': {'Nganjuk': 118, 'Kepanjen':108, 'Probolinggo':66},
    'Probolinggo': {'Lumajang': 75, 'Situbondo':100},
    'Lumajang': {'Jember': 65},
    'Jember': {'Banyuwangi': 100}
}

def ucs_with_steps(start, goal):
    frontier = [(0, start, [start])]
    explored = set()
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            # Hitung akumulasi per langkah
            step_costs = []
            total = 0
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                w = graph[u][v]
                total += w
                step_costs.append((f"{u} -> {v}", w, total))
            return path, cost, step_costs
        if node in explored:
            continue
        explored.add(node)
        for neighbor, step_cost in graph.get(node, {}).items():
            if neighbor not in explored:
                heapq.heappush(frontier, (cost + step_cost, neighbor, path + [neighbor]))
    return None, float('inf'), []

path, total_cost, steps = ucs_with_steps('Cilegon', 'Banyuwangi')

print("Jalur UCS:", path)
print("Total Biaya:", total_cost)
print("\nRincian Penjumlahan Bobot:")
for step in steps:
    print(f"{step[0]} = {step[1]} (akumulasi: {step[2]})")
