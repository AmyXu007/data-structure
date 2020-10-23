# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inOrder_help(0)
    
    return self.result

  def inOrder_help(self, index):
    if index >= self.n or index < 0:
      return
    else:
      self.inOrder_help(self.left[index])
      self.result.append(self.key[index])
      self.inOrder_help(self.right[index])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrder_help(0)  
    return self.result

  def preOrder_help(self, index):
    if index >= self.n or index < 0:
      return
    else:
      self.result.append(self.key[index])
      self.preOrder_help(self.left[index])
      self.preOrder_help(self.right[index])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postOrder_help(0)
    return self.result

  def postOrder_help(self, index):
    if index >= self.n or index < 0:
      return

    else:
      self.postOrder_help(self.left[index])
      self.postOrder_help(self.right[index])
      self.result.append(self.key[index])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
