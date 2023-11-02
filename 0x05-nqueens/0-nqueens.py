#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
  print("Usage: nqueens N")
  exit(1)

if not sys.argv[1].isdigit():
  print("N must be a number")
  exit(1)

n = int(sys.argv[1])  

if n < 4:
  print("N must be at least 4")
  exit(1)

def queens(n, row=0, cols=[], diag1=[], diag2=[]):

  if row == n:
    yield cols

  for col in range(n):
    if col not in cols and row+col not in diag1 and row-col not in diag2:
      yield from queens(n, row+1, cols+[col], diag1+[row+col], diag2+[row-col])


def solve(n):

  solutions = []
  for solution in queens(n):
    solutions.append(solution)
  
  for solution in solutions:
    print([[i, col] for i, col in enumerate(solution)])

if __name__ == "__main__":
  solve(n)
