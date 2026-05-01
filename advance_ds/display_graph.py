def display_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node} -> {', '.join(neighbors)}")

graph = {'Alex': ['Riya', 'John'], 'Riya': ['Alex']}
display_graph(graph)