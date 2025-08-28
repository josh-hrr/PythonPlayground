from collections import defaultdict;

#quick Tuples concept, they are:

#ordered
#unmutable
#heterougeouns
#allow duplicates

edges = [("A", "B"), ("A", "C"), ("B", "D")]

adj = defaultdict(list)

for u, v in edges:
  adj[u].append(v)


print(adj)

adj['C'] 
print(adj['C'])