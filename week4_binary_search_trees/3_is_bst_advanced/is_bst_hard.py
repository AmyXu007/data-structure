#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  # return True
  if not tree:
    return True
  return helper(tree, 0, float('-inf'), float('inf'))

def helper(tree, index, l, r):
  if index == -1:
    return True
  if tree[index][0] < l or tree[index][0] > r:
    return False
  else:
    return helper(tree, tree[index][1], l, tree[index][0]-1) and helper(tree, tree[index][2], tree[index][0], r)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
