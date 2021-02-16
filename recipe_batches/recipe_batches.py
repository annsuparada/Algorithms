#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #get all the keys to compare
  check_recipe_keys = recipe.keys()
  check_ingredients_keys = ingredients.keys()
  #declare batches to 0
  batches = 0
  # If ingredient not match, no batchs can be made
  if check_recipe_keys != check_ingredients_keys:
    return batches
  result = []
  for key in ingredients:
    resource = ingredients[key] / recipe[key] # find the batches number by divided 
    batches_num = int(resource) # turn float into interger
    result.append(batches_num)  # add interger to result
   
  return min(result) # get the lest batches form the ingerdients



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

