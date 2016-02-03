#!/usr/bin/env python

import random
import math
from collections import deque

"""
Write a program that does the following:

(1) Generates a random 6x6 game board. Each square in the board contains
     a single letter, chosen at random. (Given)

(2) Prints the set of legal words that can be found in the game board. A
     word is legal if it appears in wordset; a word can be
     found in the board if the letters in the word can be produced (in
     order) by starting from any square on the board and repeatedly
     moving to an adjacent square (horizontal, vertical, or diagonal
     moves are allowed; you cannot "wrap" around the edge of the board.)
     However, a single square cannot be visited more than once to form
     any given word. (Actual graph question)

"""


original_boggle_dice = ["AACIOT",
                        "AHMORS",
                        "EGKLUY",
                        "ABILTY",
                        "ACDEMP",
                        "EGINTV",
                        "GILRUW",
                        "ELPSTU",
                        "DENOSW",
                        "ACELRS",
                        "ABJMOQ",
                        "EEFHIY",
                        "EHINPS",
                        "DKNOTU",
                        "ADENVZ",
                        "BIFORX",]

def roll_dice(dice):
    return [random.choice(d) for d in random.sample(dice, len(dice))]

def matricize(lst):
    sqrt = int(math.sqrt(len(lst)))
    assert sqrt * sqrt == len(lst), "not a square"
    return [lst[i*sqrt:(i+1)*sqrt] for i in xrange(sqrt)]

def gen_board(dice):
    return matricize(roll_dice(dice))

def print_matrix(mat):
    for r in mat: print r


def spanning_chains(mat, allowed_chains):
    # The constraint on visiting only allowed once
    # makes the need for the following filter:
    possible_allowed_chains = filter(lambda x: len(set(x)) == len(x),
                                     allowed_chains)


    random.shuffle(possible_allowed_chains)
    ad_list = dict()
    width = height = len(mat)
    # Sparse thus consturct ad list
    key_counter = {}
    # O(n^2)
    for x, nodes in enumerate(mat):
        for y, node in enumerate(nodes):
            if node not in ad_list.keys():
                ad_list[node] = list()
                key_counter[node] = 1
            else:
                ad_list[node + str(key_counter[node])] = list()
                key_counter[node] += 1
                node = node + str(key_counter[node] -1)
                mat[x][y] = node
            # O(1)
            for x_ in range(max(0,x-1),min(width,x+2)):
                for y_ in range(max(0,y-1),min(height,y+2)):
                    if (x,y)==(x_,y_): continue
                    ad_list[node].append(mat[x_][y_])
    out = list()

    s = lambda d : ''.join([f for f in d if f.isalpha()])
    for j, path in enumerate(allowed_chains):
        p = filter(lambda x: x.isalpha(), list(path))

        if p[0] in ad_list.keys():
            cache = ad_list[p[0]]
            p.pop(0)

            for i, x in enumerate(p):
                if x in map(lambda y: s(y), cache):
                    k = filter(lambda y:  s(y) ==x,
                               cache)
                    cache = ad_list[k.pop()]
                    if i == len(p)-1:
                        out.append(path)

                else:
                    break;


    return out




if __name__ == "__main__":
    bmat = gen_board(original_boggle_dice)
    bmat = [['R', 'X', 'I', 'E'],
            ['O', 'F', 'I', 'A'],
            ['O', 'U', 'B', 'H'],
            ['S', 'R', 'O', 'M']]
    print_matrix(bmat)
    print spanning_chains(bmat, original_boggle_dice)
