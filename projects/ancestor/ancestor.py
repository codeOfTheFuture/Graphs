from graph import Graph
from util import Queue

def bfs(starting_vertex, graph):
    queue = Queue()
    queue.enqueue([starting_vertex])
    longest_path = [starting_vertex]

    while queue.size() > 0:
        current_path = queue.dequeue()
        current_len = len(current_path)
        longest_len = len(longest_path)
        
        if current_len > longest_len:
            longest_path = current_path
        
        if current_len == longest_len and current_path[-1] < longest_path[-1]:
            longest_path = current_path

        for next_vert in graph.get_neighbors(current_path[-1]):
            new_path = list(current_path)
            new_path.append(next_vert)
            queue.enqueue(new_path)

    if longest_path[-1] != starting_vertex:
        return longest_path[-1]
    else:
        return -1


def earliest_ancestor(ancestors, starting_node):
    gg = Graph()

    for i in ancestors:
        for j in i:
            if j not in gg.vertices:
                gg.add_vertex(j)

    for ancestor in ancestors:
        gg.add_edge(ancestor[1], ancestor[0])

    return bfs(starting_node, gg)

    
    

    