#!/bin/python3

# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import math
import os
import random
import re
import sys
import pdb;

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores_lenght, alice_lenght = len(scores), len(alice)
    scores_index, alice_index = 0, alice_lenght-1
    rank, alice_ranks, rank_incremented = 1, [], False

    while alice_index >= 0:
        if alice[alice_index] >= scores[scores_index]:
            alice_ranks.insert(0, rank)
            alice_index -= 1
        else:
            if scores_lenght-1 == scores_index:
                if not rank_incremented:
                    rank += 1
                    rank_incremented = True
                alice_ranks.insert(0, rank)
                alice_index -= 1
            else:
                scores_index += 1
                if scores[scores_index] < scores[scores_index-1]:
                    rank += 1

    return alice_ranks



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
