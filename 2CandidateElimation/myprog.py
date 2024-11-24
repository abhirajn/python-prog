 import numpy as np
import pandas as pd
import csv
[46]: # Loading dataset
X = []
y = []
with open ('c1.csv') as file:
reader = csv.reader(file)
for row in reader:
# Select every column except last column
X.append(row[:-1])
# Select last column
y.append(row[-1])
[47]: # Candidate Elimination algorithm
def learn (X, y):
# Number of attributes
n = len(X[0])
# Specific hypothesis
specific = X[0].copy()
# General hypothesis
general = [['?' for _ in range(n)] for _ in range(n)]
for i, h in enumerate(X):
if y[i] == 'Y':
for x in range (n):
if h[x] != specific[x]:
1
specific[x] = '?'
general[x][x] = '?'
elif y[i] == 'N':
for x in range (n):
if h[x] != specific[x]: general[x][x] = specific[x]
else: general[x][x] = '?'
# Remove elements from general hypothesis if its equal to [ '?', '?', '?', .
,→..., '?' ]
indices = [i for i, val in enumerate(general) if val == (['?'] * n)]
for _ in indices: general.remove(['?'] * n)
return specific, general
[48]: specific, general = learn(X,y)
print('Specific hypothesis', specific, sep='\n')
print()
print('General hypothesis', general, sep='\n')
