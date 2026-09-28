def heuristic(n):
    H_dist = {
        'A': 10,
        'B': 4
        }
    return H_dist[n]

graph_nodes = {
        'A': [('B',6)],
        'B': [('A',6),('C',3),('D',2)]
    }

def get_neighbors(v):
    return graph_nodes.get(v, [])

def A_star_algo(start_node,stop_node):
    open_set = {start_node}
    closed_set = set()

    g = {start_node : 0}
    parents = {start_node: start_node}

    while open_set:
        n = None

        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print("Path found:",path)
            print("Cost:",g[stop_node])
            return path

        for (m, weight) in get_neighbors(n):

            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                if g.get(m, float('inf')) > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)
    print("Path doesnt exist")
    return None

A_star_algo('A','B')
        
