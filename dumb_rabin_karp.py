class RabinKarp:

    @staticmethod
    def hash(string):
        """
        Simplest and dumbest hash
        """
        hs = 0
        for s in string:
            hs += ord(s)
        return hs
    
    def match(self, string, substr):
        """
        RK algorithm for mathcing a substring
        in a string returns starting index if found
        otherwise -1
        """
        hp = self.hash(substr)
        hh = self.hash(string[0:0+len(substr)])
        if hh == hp:
            if string[0:0+len(substr)] == substr:
                    return 0
        for i in xrange(1, len(string) - len(substr) + 1):
            hh = hh - ord(string[i-1]) + ord(string[i + len(substr) -1])
            if hh == hp:
                if string[i:i+len(substr)] == substr:
                    return i
        return -1
