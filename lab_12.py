graph = {
'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': set([
(7, 'A', 'B'),
(5, 'A', 'D'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(8, 'C', 'B'),
(5, 'C', 'E'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(7, 'D', 'E'),
(6, 'D', 'F'),
(7, 'E', 'B'),
(5, 'E', 'C'),
(7, 'E', 'D'),
(8, 'E', 'F'),
(9, 'E', 'G'),
(6, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'E'),
(11, 'G', 'F'),
])
}


sets = []

def print_set():
    pass

def make_set(nodes, edges = []):
    set = dict()

    set['nodes'] = nodes
    set['edges'] = edges

    return set

def get_union(set1, set2, edge = None):

    new_nodes = []
    new_nodes.extend(set1['nodes'])
    new_nodes.extend(set2['nodes'])

    new_edges = []
    new_edges.extend(set1['edges'])
    new_edges.extend(set2['edges'])

    if edge != None:
        new_edges.append(edge)

    return make_set(new_nodes, new_edges)


def find_set(p):
    for set in sets:
        if p in set['nodes']:
            return set

def kruskala(graph):
    nodes = graph['nodes']
    edges = graph['edges']

    for node in nodes:
        sets.append(make_set([node]))

    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        a = find_set(edge[1])
        b = find_set(edge[2])
        if a != b:
            sets.remove(a)
            sets.remove(b)


            new_set = get_union(a, b, edge)

            sets.append(new_set)




kruskala(graph)

print(sets)


