import math
import csv
import pandas as pd
import numpy as np


def load():
  data = csv.reader(open('prog3 .csv', 'r'));
  d = list(data)
  h = d.pop(0)
  return d,h

class Node:
  def __init__(self, attribute):
    self.attribute = attribute
    self.children = []
    self.answer = ""

def sub(data, col, delete):
  dic = {}
  # print(col, data[col])
  coldata = [row[col] for row in data]
  attr = list(set(coldata))

  for i in attr : dic[i] = []

  for i in range(len(data)):
    key = data[i][col]
    if delete : del data[i][col]
    dic[key].append(data[i])

  return attr ,dic

def entropy (row):
  attr = list(set(row))
  if len(attr) == 1: return 0;

  arr = [0] * len(attr)
  for i in range(len(attr)) : arr[i] = sum([1 for x in row if x == attr[i]])/(len(row)*1.0)
  ans = 0
  for i in arr : ans += -1*i*math.log(i,2)
  return ans

def compute_gain (data, col):
  # print("hi" ,col)
  attr, dic = sub(data, col, delete=False)
  total_entropy = entropy([row[-1] for row in data])

  for i in range(len(attr)):
    ratio = len(dic[attr[i]])/(len(data)*1.0)
    entro = entropy([row[-1] for row in dic[attr[i]]])
    total_entropy -= ratio*entro

  return total_entropy


def build_tree(data, header):
  y = [row[-1] for row in data]
  if len(set(y)) == 1:
    node = Node("")
    node.answer = y[0]
    return node

  n = len(data[0])-1
  gains = [compute_gain(data , c) for c in range(n)]
  split = gains.index(max(gains))
  node = Node(header[split])
  fea = header[:split] + header[split+1:]

  attr, dic = sub(data, split, delete=True)

  for i in range(len(attr)):
    child = build_tree(dic[attr[i]] , fea)
    node.children.append((attr[i] , child))

  return node


def print_tree (node, level):
  if node.answer != "":
    print("---"*level, node.answer)
    return
  print("---"*level, node.attribute)
  for value, n in node.children:
    print("---"*(level+1), value)
    print_tree(n, level+2)

data , header = load()


node = build_tree(data, header)

print_tree(node, 0)

data

header
