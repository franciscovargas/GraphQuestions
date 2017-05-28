
def argmin(Q, D, V):
    minn = float("inf")
    ind = -1
    for j,i in enumerate(Q):
        if i not in V:
            if D[i] < minn:
                minn = D[i]
                ind = j
    return ind


def djKestra(root, adj):
    q = adj.keys()
    visited = set([])
    cost_mat = [float("inf")] * (len(adj) + 1)
    cost_mat[root] = 0
    while q:
        arg = argmin(q, cost_mat, visited)        
        cur_node = q.pop(arg)
        visited |= {cur_node}
        
        for node in adj[cur_node]:
            if cost_mat[node] > cost_mat[cur_node] + w[(cur_node, node)]:
                cost_mat[node] = cost_mat[cur_node] + w[(cur_node, node)]
    return cost_mat
