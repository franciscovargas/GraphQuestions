from itertools import chain

def level_gen(ad_list, root, sh, h):
    """
    creats a dictionary of levels for
    a tree from an adjecency list representation
    of a graph
    """
    if sh == 0:
        return {0: [root]}
    else:
        level = h - sh
        cache = ad_list[root]
        ad_list[root] = list(chain(*[ad_list[x] for x in ad_list[root] ]))
        a = level_gen(ad_list,root, sh-1,h)
        a[level+1]  = cache
    return a


def find_depth(ad_list, root):
    """
    Find the height of the tree
    from an adjecency list representation of
    a graph
    """
    if len(ad_list[root]) < 1:
        return 0
    else:
        return max([find_depth(ad_list, x) + 1 for x in ad_list[root] ])


if __name__ == "__main__":
    d = dict()
    d['A'] = ['B', 'C']
    d['B'] = ['D', 'E']
    d['C'] = ['F', 'G']
    d['D'] = []
    d['E'] = []
    d['F'] = []
    d['G'] = []
    h = find_depth(d, 'A')
    print level_gen(d, 'A', h, h)
