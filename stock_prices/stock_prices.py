#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price = prices[0]
  profit = -prices[0]
  i = 0 #just for print
  for num in prices:
    i += 1 #just for print
    print(f'---------loop: {i}--------')
    print(f'num: {num}')
    if num - current_min_price > profit and prices.index(num) != 0:
      print(f'prices.index(num): {prices.index(num)}')
      profit = num - current_min_price
      print(f'current_min_price: {current_min_price}')
    if num < current_min_price:
      current_min_price = num
  
    print(f'profit: {profit}')
  return profit

print(find_max_profit([5, 8, 1, 30, 66]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
