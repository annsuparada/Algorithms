#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choises = ['rock', 'paper', 'scissors'] 
  results = []
  
  def add_n(n, result=[]):
    if n == 0:
      return results.append(result)
    for i in choises:
      print(f'i: {i}')
      add_n(n-1, result + [i])

  add_n(n, [])
  return results

print(f' print:{rock_paper_scissors(2)}')

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')