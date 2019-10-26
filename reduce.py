#!/usr/bin/python
#@author:Rahul Gahlot <gahlotrl@mail.uc.edu>


import sys
from collections import defaultdict
#capture values from the mapper using unique keys
keys = [
        "key1",
        "key2",
        "key3",
        "key4",
        "key5",
        "key6",
        "key7",
        "key8"
        ]

#Dictionary to store our result
values = defaultdict(dict)

for line in sys.stdin:
  #split the string
  line = line.strip()
  #split the string with delimiter
  arrayofkeys = line.split('\t')
  #remove element from index
  problem = arrayofkeys.pop(0).strip()
  column = arrayofkeys.pop(0).strip()

  #add key to dictionary and sum the values
  if problem not in values.keys():
    values[problem][column] = sum([int(x) for x in arrayofkeys])
  else:
    if column not in values[problem].keys():
      values[problem][column] = sum([int(x) for x in arrayofkeys])
    else:
      values[problem][column] += sum([int(x) for x in arrayofkeys])

#print the maximum number values of keys	  
for x, key in enumerate(keys):
  max_key = max(values[key], key=values[key].get)
  print("solution{}: {} {}".format(x+1, max_key, values[key][max_key]))

