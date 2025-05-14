def prefix(kmer):
    return kmer[:-1]

def suffix(kmer):
    return kmer[1:]

def path_graph(text, k, d):
    graph = {}
    nodes = set()

    for i in range(len(text) - 2 * k - d + 1):
        kmer = text[i:i + 2 * k + d]
        prefix_node = prefix(kmer)
        suffix_node = suffix(kmer)

        if prefix_node not in graph:
            graph[prefix_node] = []
        if suffix_node not in graph:
            graph[suffix_node] = []

        graph[prefix_node].append((kmer, suffix_node))
        nodes.add(prefix_node)
        nodes.add(suffix_node)

    return graph, nodes

text = "TAATGCCATGGGATGTT"
k = 3
d = 1

path_graph_result, nodes_result = path_graph(text, k, d)

for node in nodes_result:
    if node in path_graph_result:
        for edge in path_graph_result[node]:
            print(f"{node} -> {edge[1]} [{edge[0]}]")
