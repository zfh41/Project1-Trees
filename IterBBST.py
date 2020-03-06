import random
import time

class Node:
  def __init__(Node, value):
    Node.value = value
    Node.right = None
    Node.left = None
    Node.height = 1

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

def getBF(node):
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
  

def deleteIter(root, value):
    returnValue = None
    curr = root
    parentNode = None
    isLeft = None
    appendList = list()
    while True:
      appendList.append(curr)
      if curr.value == value:
        break
      if value < curr.value and curr.left is not None:
        parentNode = curr
        curr = curr.left
        isLeft = True
      elif value > curr.value and curr.right is not None:
        parentNode = curr
        curr = curr.right
        isLeft = False
      else:
        returnValue = root
        break
    while True:
      c = curr
      if c.left is None and c.right is None:
        if parentNode is None:
          returnValue = None
          break
        elif isLeft:
          parentNode.left = None
        else:
          parentNode.right = None
        returnValue = root
        break
      elif c.left is None:
        if isLeft is None:
          returnValue = root.right
          break
        elif isLeft:
          parentNode.left = c.right
        elif not isLeft:
          parentNode.right = c.right
        returnValue = root
        break
      elif c.right is None:
        if isLeft is None:
          returnValue = root.left
          break
        elif isLeft:
          parentNode.left = c.left
        elif not isLeft:
          parentNode.right = c.left
        returnValue = root
        break
      else:
        parentNode = c
        rightNode = c.right
        appendList.append(rightNode)
        isLeft = False
        while thingtoDelete.left is not None:
          parentNode = thingtoDelete
          thingtoDelete = rightNode.left
          isLeft = True
          appendList.append(rightNode)
        c.value = rightNode.value
        curr = rightNode
    while len(appendList) != 0:
      a = appendList.pop()
      a.height = max(getHeight(a.left), getHeight(a.right)) + 1
      balance = getBF(a)
      if balance > 1:
        leftBalance = getBF(a.left)
        if leftBalance < 0:
          if len(appendList) == 0:
            returnValue = leftRightRotate(a)
          else:
            if appendList[-1].left == a:
              appendList[-1].left = leftRightRotate(a)
            else:
              appendList[-1].right = leftRightRotate(a)
        elif leftBalance >= 0:
          if len(appendList) == 0:
            returnValue = rightRotate(a)
          else:
            if appendList[-1].left == a:
              appendList[-1].left = rightRotate(a)
            else:
              appendList[-1].right = rightRotate(a)
      elif balance < -1:
        rightBalance = getBF(a.right)
        if rightBalance <= 0:
          if len(appendList) == 0:
            returnValue = leftRotate(a)
          else:
            if appendList[-1].left == a:
              appendList[-1].left = leftRotate(a)
            else:
              appendList[-1].right = leftRotate(a)
        elif rightBalance > 0:
          if len(appendList) == 0:
            returnValue = rightLeftRotate(a)
          else:
            if appendList[-1].left == a:
              appendList[-1].left = rightLeftRotate(a)
            else:
              appendList[-1].right = rightLeftRotate(a)
    return returnValue


def insertIter(root, value):
  count = 0
  curr = root
  appendList=list()
  while True:
    appendList.append(curr)
    if value < curr.value:
      if curr.left is None:
        curr.left = Node(value)
        break
      count = count+1
      curr = curr.left
    elif value > curr.value:
      if curr.right is None:
        curr.right = Node(value)
        break
      count=count+1
      curr = curr.right
    else:
      return False
  while len(appendList) != 0:
    a = appendList.pop()
    a.height = max(getHeight(a.left), getHeight(a.right)) + 1
    balance = getBF(a)
    if balance > 1:
      leftBalance = getBF(a.left)
      if leftBalance == -1:
        if len(appendList) == 0:
          root = leftRightRotate(a)
        else:
          if appendList[-1].left == a:
            appendList[-1].left = leftRightRotate(a)
          else:
            appendList[-1].right = leftRightRotate(a)
      elif leftBalance == 1:
        if len(appendList) == 0:
          root = rightRotate(a)
        else:
          if appendList[-1].left == a:
            appendList[-1].left = rightRotate(a)
          else:
            appendList[-1].right = rightRotate(a)
    elif balance < -1:
      rightBalance = getBF(a.right)
      if rightBalance == -1:
        if len(appendList) == 0:
          root = leftRotate(a)
        else:
          if appendList[-1].left == a:
            appendList[-1].left = leftRotate(a)
          else:
            appendList[-1].right = leftRotate(a)
      elif rightBalance == 1:
        if len(appendList) == 0:
          root = rightLeftRotate(a)
        else:
          if appendList[-1].left == a:
            appendList[-1].left = rightLeftRotate(a)
          else:
            appendList[-1].right = rightLeftRotate(a)
  return root, count



def findNextChildIter(root):
    while root.left is not None:
      root = root.left
    return root

def findNextAncestorIter(root, value):
    curr = root
    while True:
      if ((curr.left is None or root.left.value <= value) and curr.value > value):
        return curr
      if curr.left is not None and value < curr.value:
        curr = curr.left
      elif curr.right is not None and value > curr.value:
        curr = curr.right
      # an ancestor with value greater than the provided was not found
      else:
        return None

def findNextIter(root, value):
    node = findIter(root, value)
    if node is None:
      return None
    elif node.right is None:
      return findNextAncestorIter(root, value)
    return findNextChildIter(node.right)

def findPrevChildIter(root):
    while root.right is not None:
      root = root.right
    return root

def findPrevAncestorIter(root, value):
    curr = root
    while True:
      if ((curr.right is None or root.right.value >= value) and curr.value < value):
        return curr
      if curr.left is not None and value < curr.value:
        curr = curr.left
      elif curr.right is not None and value > curr.value:
        curr = curr.right
      # an ancestor with value lesser than the provided was not found
      else:
        return None

def findPrevIter(root, value):
    node = findIter(root, value)
    if node is None:
      return None
    elif node.left is None:
      return findPrevAncestorIter(root, value)
    return findPrevChildIter(node.left)

def Inorder(node):
    if node is not None:
      Inorder(node.left)
      print(node.value)
      Inorder(node.right)
      
def getRandomArray(n):
  random_array = list()
  for i in range(n):
    random_int = getRandomNumber(n)
    while random_int in random_array:
      random_int = getRandomNumber(n)
    random_array.append(random_int)
  return random_array

def getRandomNumber(n):
  return random.randint(0, n*10)

def getSortedArray(n):
  sorted_array = list()
  for i in range(n, 0, -1):
    sorted_array.append(i)
  return sorted_array
  


def main():
    arr = getRandomArray(10000)
    root = Node(arr[0])
    for i in range(1, len(arr), 1):
      root = insertIter(root, arr[i])[0]
    Inorder(root);
    
    
    
    
    total = 0
    arr = getSortedArray(10000)
    root = Node(arr[0])
    for i in range(1, len(arr), 1):
      x = insertIter(root, arr[i])
      root = x[0]
      total += x[1]
    print(total)

if __name__ == "__main__":
    main()


