import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    G = nx.Graph()

    G.add_edge('a','d',weight=2)
    G.add_edge('a','c',weight=1)

    G.add_edge('b','c',weight=2)
    G.add_edge('b','f',weight=3)

    G.add_edge('c','a',weight=1)
    G.add_edge('c','d',weight=1)
    G.add_edge('c','e',weight=3)
    G.add_edge('c','b',weight=2)

    G.add_edge('d','a',weight=2)
    G.add_edge('d','c',weight=1)
    G.add_edge('d','g',weight=1)

    G.add_edge('e','c',weight=3)
    G.add_edge('e','f',weight=2)
    G.add_edge('g','d',weight=1)
    G.add_edge('g','f',weight=1)

    return G


def dijkstra(graph, start,end):
    unvisited = {start}
    visited = set()
    dist = {start: 0}
    parents = {}

    while unvisited:
        curr = min(
            [(dist[node], node) for node in unvisited]
        )[1]

        if curr == end:
            break

        unvisited.discard(curr)
        visited.add(curr)

        edges = [i for i in graph.neighbors(curr)]

        u_neighbours = set(edges).difference(visited)
        for neigh in u_neighbours:
            neighbour_distance = dist[curr] + graph.get_edge_data(curr,neigh)['weight']
            if neighbour_distance < dist.get(neigh,float('inf')):
                dist[neigh] = neighbour_distance
                parents[neigh] = curr
                unvisited.add(neigh)

    print(dist)
    return _deconstruct_path(parents, end)

def _deconstruct_path(parents, end):
    if end not in parents:
        return None
    cursor = end
    path = []
    while cursor:
        path.append(cursor)
        cursor = parents.get(cursor)
    return list(reversed(path))


graph = create_graph()

print(dijkstra(graph,'a','f'))

nx.draw(graph,with_labels=True)
plt.show()
