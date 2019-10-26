#!/usr/bin/python

import csv
import sys
from collections import defaultdict

#create a enumerate class to define unique names
class loc():
  date = 0
  borough = 1
  zip = 2
  person_i = 3
  person_k = 4
  ped_i = 5
  ped_k = 6
  cyc_i = 7
  cyc_k = 8
  mtr_i = 9
  mtr_k = 10
  vehi_type = 11

for x, line in enumerate(sys.stdin):
  if x == 0:
    continue
  # remove extra spaces from the line
  line = line.strip()
  line = line.split(",")

  # Date on which maximum number of accidents took place.
  print("key1 \t {} \t {} \t {}".format(line[loc.date],
               line[loc.person_i],
               line[loc.person_k],
               ))

  # Borough with maximum count of accident fatality
  print("key2 \t {} \t {}".format(line[loc.borough],
             line[loc.person_k]
             ))

  # Zip with maximum count of accident fatality
  print("key3 \t {} \t {}".format(line[loc.zip],
             line[loc.person_k]
             ))

  # vehicle type involved in maximum accidents
  print("key4 \t {} \t {}".format(line[loc.vehi_type],
             line[loc.person_k],
             line[loc.person_i]
             ))

  # key instead of date
  year = line[loc.date].split("/")[2]
  # Year in which maximum Number Of Persons and Pedestrians Injured with duplicate pedestrian value as person also include pedestrians
  print("key5 \t {} \t {} \t {}".format(year,
             line[loc.person_i],
             line[loc.ped_i]
             ))

  # Year in which maximum Number Of Persons and Pedestrians killed with duplicate pedestrian value as person also include pedestrians
  print("key6 \t {} \t {} \t {}".format(year,
             line[loc.person_k],
             line[loc.ped_k]
             ))
  # Year in which maximum Number Of Cyclist Injured and Killed (combined)
  print("key7 \t {} \t {} \t {}".format(year,
             line[loc.cyc_i],
             line[loc.cyc_k]
             ))
  # Year in which maximum Number Of Motorist Injured and Killed (combined)
  print("key8 \t {} \t {} \t {}".format(year,
             line[loc.mtr_i],
             line[loc.mtr_k]
             ))

