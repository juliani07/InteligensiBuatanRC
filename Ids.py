graph = {
    'Cilegon': {'Tangerang': 81},
    'Tangerang': {'Jakarta': 29},
    'Jakarta': {'Bekasi': 22, 'Depok': 25},
    'Bekasi': {'Depok': 41, 'Subang': 95, 'Indramayu': 185},
    'Depok': {'Bogor': 44},
    'Bogor': {'Sukabumi': 57},
    'Sukabumi': {'Bandung': 93},
    'Bandung': {'Tasikmalaya': 83, 'Cirebon': 106},
    'Subang': {'Cirebon': 103},
    'Indramayu': {'Cirebon': 56},
    'Tasikmalaya': {'Cilacap': 96, 'Purwokerto': 113},
    'Cirebon': {'Tegal': 71},
    'Cilacap': {'Kebumen': 70, 'Purwokerto': 42},
    'Purwokerto': {'Kebumen': 51, 'Magelang': 107, 'Tegal': 65},
    'Tegal': {'Purwokerto': 65, 'Pekalongan': 70},
    'Kebumen': {'Yogyakarta': 81},
    'Yogyakarta': {'Pacitan': 107, 'Surakarta': 75, 'Magelang': 40},
    'Pacitan': {'Trenggalek': 106},
    'Trenggalek': {'Kepanjen': 114, 'Nganjuk': 108},
    'Kepanjen': {'Lumajang': 116},
    'Pekalongan': {'Semarang': 83},
    'Magelang': {'Ambarawa': 35, 'Yogyakarta': 40},
    'Ambarawa': {'Surakarta': 70, 'Semarang': 37},
    'Semarang': {'Kudus': 60},
    'Surakarta': {'Ngawi': 83},
    'Kudus': {'Rembang': 62},
    'Rembang': {'Bojonegoro': 103, 'Tuban': 93},
    'Tuban': {'Surabaya': 95},
    'Surabaya': {'Bojonegoro': 111, 'Sidoarjo': 35},
    'Sidoarjo': {'Nganjuk': 118, 'Kepanjen': 108, 'Probolinggo': 66},
    'Probolinggo': {'Lumajang': 75, 'Situbondo': 100},
    'Lumajang': {'Jember': 65},
    'Jember': {'Banyuwangi': 100}
}


def dls(node, goal, depth, visited):
    if depth == 0:
        return [node] if node == goal else None
    if node == goal:
        return [node]
    for nb in graph.get(node, {}):
        if nb in visited:
            continue
        res = dls(nb, goal, depth - 1, visited | {nb})
        if res:
            return [node] + res
    return None

def ids(start, goal, max_depth=30):
    for depth in range(max_depth+1):
        path = dls(start, goal, depth, {start})
        if path:
            return path
    return None

def path_cost(path):
    if not path:
        return float('inf')
    cost = 0
    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        cost += graph[a][b]
    return cost

start, goal = 'Cilegon', 'Banyuwangi'
path = ids(start, goal, max_depth=30)
print("IDS Path:", path)
print("IDS Cost:", path_cost(path))

