"""
Efficient time palindrome generation
small fun puzzle.
"""
def gen_hours():
    # 70 iterations as opposed to the ~ 1400
    # brute force solution
    palindromes = list()
    for i in range(24):
        if i < 10:
            for j in range(6):
                palindromes.append("{0}:{1}{2}".format(i,j,i))

        else:
            char_array = str(i)
            if int(char_array[1]) < 6:
                palindromes.append("{0}{1}:{1}{0}".format(char_array[0],
                                                          char_array[1]))

    return palindromes



def palindrome(x):
    x = x.replace(":","")
    return x == x[::-1]


def brute_force():
    palindromes = list()
    for i in range(24):
        for j in range(60):
            if j < 10:
                j = "0" + str(j)
            hour = str(i) + ":" + str(j)
            if palindrome(hour):
                palindromes.append(hour)
    return palindromes

if __name__ == "__main__":
    p1 = gen_hours()
    p2 = brute_force()
    print all(map(palindrome, p1))
    print  len(p1), len(p2)
    print  p1
    print set(p2) -(set(p1))
