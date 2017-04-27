from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q1 = deque([])
        self._q2 = deque([])
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self._q1:
            self._q1.appendleft(x)
        else:
            self._q2.appendleft(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        qref = self._q1 if self._q1 else self._q2
        qref2 = self._q1 if not self._q1 else self._q2
        elem = qref.pop()
        while qref:
            qref2.appendleft(elem)
            elem = qref.pop()
        return elem
            

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        qref = self._q1 if self._q1 else self._q2
        qref2 = self._q1 if not self._q1 else self._q2
        while qref:
            elem = qref.pop()
            qref2.appendleft(elem)
        return elem
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._q1 and not  self._q2
