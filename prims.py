import heapq as h


def relax(y,z,parents, weights, inMST,G,W,q):
    w = W[(y,z)]
    if weights[z-1] == float("inf"):
        weights[z-1] = w
        parents[z-1] = y
        h.heappush(q, (w,z))
    elif w < weights[z-1] and not inMST[z-1]:
        weights[z-1] = w
        parents[z-1] = y
        h.heappush(q, (w,z))
        # hack for decrease queue in continue
        


def prims(G,W,s):
    parents = [None] * len(G)
    weights = [float("inf")] * len(G)
    inMST = [False] * len(G)
    
    q = []
    h.heappush(q, (0, s)) 
    
    weights[s-1] = 0
    
    while q:
        w_y, y = h.heappop(q)
        # print y
        if inMST[y-1]:
            continue # decrease key hack
        inMST[y-1] = True
        for z in G[y]:
            relax(y,z,parents, weights, inMST, G, W,q)
    val = 0
    for i in xrange(len(parents)):
        x = parents[i]
        if x is not None:
            val += W[(x, i + 1)] 
    return val
