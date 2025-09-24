import heapq

# === Graph (dengan Subang sebagai penghubung Bekasi dan Cirebon) ===
graph = {
    "Cilegon": [("Tangerang", 81)],
    "Tangerang": [("Cilegon", 81), ("Jakarta", 29)],
    "Jakarta": [("Tangerang", 29), ("Bekasi", 22), ("Depok", 25)],
    "Bekasi": [("Jakarta", 22), ("Subang", 90)],
    "Depok": [("Jakarta", 25), ("Bogor", 41)],
    "Bogor": [("Depok", 41), ("Sukabumi", 57), ("Bandung", 93)],
    "Sukabumi": [("Bogor", 57), ("Bandung", 93)],
    "Bandung": [("Sukabumi", 93), ("Purwokerto", 106), ("Cilacap", 96), ("Subang", 62)],
    "Subang": [("Bandung", 62), ("Cirebon", 57), ("Bekasi", 90)],
    "Cirebon": [("Subang", 57), ("Indramayu", 56), ("Tegal", 71)],
    "Indramayu": [("Cirebon", 56)],
    "Tegal": [("Cirebon", 71), ("Pekalongan", 70), ("Purwokerto", 65)],
    "Pekalongan": [("Tegal", 70), ("Semarang", 83)],
    "Semarang": [("Pekalongan", 83), ("Ambarawa", 37), ("Kudus", 60)],
    "Ambarawa": [("Semarang", 37), ("Magelang", 35)],
    "Magelang": [("Ambarawa", 35), ("Yogyakarta", 90), ("Surakarta", 75)],
    "Yogyakarta": [("Magelang", 90), ("Kebumen", 81), ("Pacitan", 107)],
    "Purwokerto": [("Bandung", 106), ("Tasikmalaya", 113), ("Cilacap", 51), ("Tegal", 65)],
    "Cilacap": [("Purwokerto", 51), ("Kebumen", 70)],
    "Kebumen": [("Cilacap", 70), ("Yogyakarta", 81)],
    "Surakarta": [("Magelang", 75), ("Ngawi", 83), ("Yogyakarta", 78)],
    "Ngawi": [("Surakarta", 83), ("Nganjuk", 73)],
    "Nganjuk": [("Ngawi", 73), ("Kepanjen", 114), ("Bojonegoro", 72)],
    "Bojonegoro": [("Nganjuk", 72), ("Tuban", 103), ("Surabaya", 111)],
    "Tuban": [("Bojonegoro", 103)],
    "Surabaya": [("Bojonegoro", 111), ("Sidoarjo", 35), ("Probolinggo", 108)],
    "Sidoarjo": [("Surabaya", 35), ("Probolinggo", 66)],
    "Probolinggo": [("Sidoarjo", 66), ("Situbondo", 100), ("Banyuwangi", 75)],
    "Situbondo": [("Probolinggo", 100), ("Banyuwangi", 88)],
    "Banyuwangi": [("Probolinggo", 75), ("Situbondo", 88), ("Jember", 100)],
    "Kepanjen": [("Nganjuk", 114), ("Lumajang", 116)],
    "Lumajang": [("Kepanjen", 116), ("Jember", 65)],
    "Jember": [("Lumajang", 65), ("Banyuwangi", 100)],
    "Trenggalek": [("Pacitan", 106), ("Kepanjen", 114)],
    "Pacitan": [("Yogyakarta", 107), ("Trenggalek", 106)]
}

# === Heuristic (h) ke Banyuwangi ===
h = {
    "Cilegon": 950, "Tangerang": 882, "Jakarta": 861, "Bekasi": 840,
    "Depok": 858, "Bogor": 852, "Sukabumi": 832, "Bandung": 780,
    "Subang": 750, "Indramayu": 700, "Cirebon": 662, "Tasikmalaya": 684,
    "Tegal": 595, "Purwokerto": 571, "Cilacap": 592, "Pekalongan": 537,
    "Kebumen": 521, "Magelang": 463, "Semarang": 455, "Ambarawa": 445,
    "Yogyakarta": 440, "Kudus": 416, "Surakarta": 396, "Rembang": 373,
    "Ngawi": 334, "Pacitan": 357, "Bojonegoro": 298, "Tuban": 295,
    "Nganjuk": 276, "Trenggalek": 289, "Surabaya": 210, "Sidoarjo": 196,
    "Kepanjen": 197, "Probolinggo": 132, "Lumajang": 122,
    "Situbondo": 70, "Jember": 71, "Banyuwangi": 0
}

# === Algoritma A* ===
def astar(graph, h, start, goal):
    frontier = [(h[start], 0, start, [start])]  # (f, g, node, path)
    best_cost = {start: 0}

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if node == goal:
            return path, g

        if g > best_cost.get(node, float('inf')):
            continue

        for (neigh, w) in graph.get(node, []):
            new_g = g + w
            f_new = new_g + h.get(neigh, float('inf'))
            if new_g < best_cost.get(neigh, float('inf')):
                best_cost[neigh] = new_g
                heapq.heappush(frontier, (f_new, new_g, neigh, path + [neigh]))

    return None, float('inf')

# === Main Program ===
if _name_ == "_main_":
    start = "Cilegon"
    goal = "Banyuwangi"
    path, cost = astar(graph, h, start, goal)

    print("A* Search")
    print("Start:", start)
    print("Goal :", goal)
    print("Path :", " -> ".join(path))
    print("Cost :", cost)
