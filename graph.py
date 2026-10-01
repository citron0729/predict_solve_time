import torch

def literal_to_node(literal, num_vars):
    if literal > 0:
        return literal - 1
    else:
        return abs(literal) + num_vars - 1

clauses = [
    [1, -2],
    [-1, 3],
    [2, 3]
]

num_vars = 3
num_clauses = len(clauses)

print("変数数：", num_vars)
print("節数", num_clauses)

for i, clause in enumerate(clauses):
    print("節", i + 1, ":", clause)

for i, clause in enumerate(clauses):
    print("節", i + 1, "のリテラル数:", len(clause))

edges = []

for clause_index, clause in enumerate(clauses):
    for literal in clause:
        node_index = literal_to_node(literal, num_vars)
        clause_node = 2 * num_vars + clause_index
        edges.append((node_index, clause_node))
        edges.append((clause_node, node_index))

for edge in edges:
    print(edge)

edge_index = torch.tensor(edges, dtype=torch.long).t()

print(edge_index)
print(edge_index.shape)

num_nodes = 2 * num_vars + num_clauses

x = torch.zeros((num_nodes, 3))

for i in range(num_nodes):
    if i < num_vars:
        x[i][0] = 1

    elif i < 2 * num_vars:
        x[i][1] = 1

    else:
        x[i][2] = 1

print(x)

aggregated = torch.zeros_like(x)

for source, target in edges:
    aggregated[target] += x[source]

print(aggregated)