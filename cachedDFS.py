from collections import deque
from itertools import chain

def constructAdList(mat):
    """
    COnstruct non sparse representation of graph
    """
    m = len(mat)
    ad_list = dict()
    for i in xrange(m):
        for j in xrange(m):
            node = mat[i][j]
            ad_list[node] = list()
            for x in xrange(max(0,i-1),
                            min(i+1,m-1) +1):
                x_neigh = mat[x][j]
                if(abs(x_neigh - node) == 1):
                    ad_list[node].append(x_neigh)
            for y in xrange(max(0,j-1),
                            min(j+1,m-1) + 1):
                y_neigh = mat[i][y]
                if(abs(y_neigh - node) == 1):
                    ad_list[node].append(y_neigh)

    return ad_list

def bfsMax(node, adj_list):
    """
    Traverse Graph for all, TODO:longest path | node
    """
    s = deque()
    q = deque()
    s.append(node)
    q.appendleft(node)
    hash_cache = set([node])
    paths = list()
    tmp_chain = list()
    while(len(s) > 0):
        cur_node = s.pop()
        tmp_chain.append(cur_node)
        # find root of search and clear tmp_path
        if(len(s) > 0
           and len(adj_list[cur_node]) == 1
           and adj_list[cur_node][0] in hash_cache):
            # obtain parent of next scheduled search
            root = q.pop()
            ind = tmp_chain.index(root)
            # derreference and store
            paths.append(list(tmp_chain))
            # use parent to hop back
            tmp_chain = tmp_chain[:ind+1]
        for child in adj_list[cur_node]:
            if(child not in hash_cache):
                s.append(child)
                q.appendleft(child)
                hash_cache = hash_cache.union([child])
    paths.append(tmp_chain)
    return paths

def main():
    mat = [[1,2,3],
           [6,5,4],
           [7,8,9]]
    adj =constructAdList(mat)
    print(adj)
    nodes = chain(*mat)
    for node in nodes:
        print( bfsMax(node, adj))

if __name__ == '__main__':
    main()
