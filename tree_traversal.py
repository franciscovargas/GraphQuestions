from collections import deque

class B(object):
    def __init__(self, L, R, name):
            self. L = L
            self.R = R
            self.name = name

# tree = B(B(B(None, None, "D"), B(None, None, "E"), "B"), B(B(None, None,"F"), B(None, None, "G"), "C"), "A")
tree = B(B(B(None, None, "D"),
           B(None, None, "E"), "B"),
         B(B(None, None,"F"),
           B(None, None, "G"), "C"), "A")
print tree.name

q = deque()
q.append(tree)
print q

while len(q)>0:
    node = q.pop()
    print node.name
    if node.L is not None:
        q.appendleft(node.L)
    if node.R is not None:
        q.appendleft(node.R)

print 'Depth:'
q.append(tree)
while len(q)>0:
    node = q.pop()
    print node.name
    if node.L is not None:
        q.append(node.L)
    if node.R is not None:
        q.append(node.R)
