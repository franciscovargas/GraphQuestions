from collections import deque

g = dict()
g['A'] = ['B','C']
g['B'] = ['A','C','D','E']
g['C'] = ['B','A','F','G']
g['D'] = []
g['E'] = []
g['F'] = []
g['G'] = []

print g

visited = {'A'}
q = deque()
q.append('A')

while q:
    node = q.pop()
    print node
    for e in g[node]:
        if e not in visited:
            visited.append(e)
            q.appendleft(e)
