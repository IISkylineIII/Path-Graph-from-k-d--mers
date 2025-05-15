# Path-Graph-from-k-d--mers

# Description
This Python script generates a path graph from a DNA sequence using (k,d)-mers. The graph illustrates how (k,d)-mer substrings connect through overlapping prefix and suffix nodes, providing a foundation for understanding genome assembly strategies.

# Usage
Example
```

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

# Example usage
text = "TAATGCCATGGGATGTT"
k = 3
d = 1

path_graph_result, nodes_result = path_graph(text, k, d)

# Print the graph
for node in nodes_result:
    if node in path_graph_result:
        for edge in path_graph_result[node]:
            print(f"{node} -> {edge[1]} [{edge[0]}]")

```
# Output

TGCCAT -> GCCATG [TGCCATG]
GCCATG -> CCATGG [GCCATGG]
GGGATG -> GGATGT [GGGATGT]
ATGGGA -> TGGGAT [ATGGGAT]
CATGGG -> ATGGGA [CATGGGA]
TGGGAT -> GGGATG [TGGGATG]
GGATGT -> GATGTT [GGATGTT]
CCATGG -> CATGGG [CCATGGG]
AATGCC -> ATGCCA [AATGCCA]
TAATGC -> AATGCC [TAATGCC]
ATGCCA -> TGCCAT [ATGCCAT]

# Function Descriptions
* prefix(kmer): Returns the prefix of a (k,d)-mer.
* suffix(kmer): Returns the suffix of a (k,d)-mer.
* path_graph(text, k, d): Constructs a path graph from the input sequence text using (k,d)-mers.

# Applications
* Visualization of (k,d)-mer overlaps in genome assembly.
* Educational tool for understanding graph-based sequence analysis.
* Foundations for De Bruijn graph algorithms.

# License
This project is licensed under the MIT License.

