import random
import time


class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1

def findMinIter(root):
    while root.left is not None:
      root = root.left
    return root

def findMaxIter(root):
    while root.right is not None:
      root = root.right
    return root

def getHeight(node):
  if not node:
      return 0
  return node.height

def getBalance(node):
  if not node:
      return 0
  return getHeight(node.left) - getHeight(node.right)

def leftRotate(node):
  temp = node.right
  node.right = temp.left
  temp.left = node
  node.height = max(getHeight(node.left), getHeight(node.right)) + 1
  temp.height = max(getHeight(temp.left), getHeight(temp.right)) + 1
  return temp

def rightRotate(node):
  temp = node.left
  node.left = temp.right
  temp.right = node
  node.height = max(getHeight(node.left), getHeight(node.right)) + 1
  temp.height = max(getHeight(temp.left), getHeight(temp.right)) + 1
  return temp

def leftRightRotate(node):
  node.left = leftRotate(node.left)
  return rightRotate(node)

def rightLeftRotate(node):
  node.right = rightRotate(node.right)
  return leftRotate(node)
  

def insertRecAVL(root, value): # recursive insert is broken
  if value < root.value:
    if root.left is None:
      root.left = Node(value)
    else:
      insertRecAVL(root.left, value)
  else:
    if root.right is None:
      root.right = Node(value)
    else:
      insertRecAVL(root.right, value)
  root.height = max(getHeight(root.left), getHeight(root.right)) + 1
  balance = getBalance(root)
  if balance > 1:
      leftBalance = getBalance(root.left)
      if leftBalance == -1:
        return leftRightRotate(root)
      elif leftBalance == 1:
        return rightRotate(root)
  elif balance < -1:
    rightBalance = getBalance(root.right)
    if rightBalance == -1:
      return leftRotate(root)
    elif rightBalance == 1:
      return rightLeftRotate(root)
  return root


def deleteRecAVL(root, value):
    if root is None: return root
    if value > root.value and root.right is not None:
      root.right = deleteRecAVL(root.right, value)
    elif value < root.value and root.left is not None:
      root.left = deleteRecAVL(root.left, value)
    else:
      if root.left is None:
        x = root.right
        root = None
        return x
      elif root.right is None:
        x = root.left
        root = None
        return x
      elif root.right is not None:
        inorder_successor = findMinIter(root.right)
        root.value = inorder_successor.value
        root.right = deleteRecAVL(root.right, inorder_successor.value)
    root.height = max(getHeight(root.left), getHeight(root.right)) + 1
    balance = getBalance(root)
    if balance > 1:
      leftBalance = getBalance(root.left)
      if leftBalance < 0:
        return leftRightRotate(root)
      else:
        return rightRotate(root)
    elif balance < -1:
      rightBalance = getBalance(root.right)
      if rightBalance > 0:
        return rightLeftRotate(root)
      else:
        return leftRotate(root)
    return root

def getRandomArray(n):
    randArray = list()
    for i in range(n):
      randint = random.randint(0, 1000);
      while randint in randArray:
        randint = random.randint(0, 1000);
      randArray.append(randint)
    return randArray


def getSortedArray(n):
  sorted_array = list()
  for i in range(n, 0, -1):
    sorted_array.append(i)
  return sorted_array

    
    



