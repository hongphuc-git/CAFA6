from goatools.obo_parser import GODag
import networkx as nx
import matplotlib.pyplot as plt

# ================================
# 1. Load file OBO
# ================================
obo_path = "Train/go-basic.obo"     
go = GODag(obo_path)

# ================================
# 2. Chọn 1 GO term để vẽ subtree
# ================================
root_id = "GO:0008150"  # Biological Process
# root_id = "GO:0003674"  # Molecular Function
# root_id = "GO:0005575"  # Cellular Component

root_term = go[root_id]

# Lấy toàn bộ children (tối đa depth = 2 để hình không quá lớn)
def get_children(term, depth=2):
    if depth == 0:
        return set()
    s = set(term.children)
    for c in term.children:
        s |= get_children(c, depth-1)
    return s

children = get_children(root_term, depth=2)   #chỉnh depth nếu muốn
nodes = {root_term} | children

# ================================
# 3. Build graph
# ================================
G = nx.DiGraph()

for term in nodes:
    G.add_node(term.id, label=term.name)
    for parent in term.parents:
        if parent in nodes:
            G.add_edge(parent.id, term.id)

# ================================
# 4. Vẽ Graph
# ================================
plt.figure(figsize=(14, 10))

pos = nx.spring_layout(G, k=0.5, iterations=50)

nx.draw(
    G,
    pos,
    with_labels=False,
    node_size=150,
    arrowsize=8,
)

# Thêm label
labels = {n: G.nodes[n]["label"] for n in G.nodes}
nx.draw_networkx_labels(G, pos, labels, font_size=6)

plt.title(f"Sub-graph of GO from root {root_id} ({root_term.name})")
plt.show()
