#State capitals quiz game

import sys
import random

capdic = {
'Alabama' : 'Montgomery',
'Alaska' : 'Juneau',
'Arizona' : 'Phoenix',
'Arkansas' : 'Little Rock',
'California' : 'Sacramento',
'Colorado' : 'Denver',
'Connecticut' : 'Hartford',
'Delaware' : 'Dover',
'Florida' : 'Tallahassee',
'Georgia' : 'Atlanta',
'Hawaii' : 'Honolulu',
'Idaho' : 'Boise',
'Illinois' : 'Springfield',
'Indiana' : 'Indianapolis',
'Iowa' :	'Des Moines',
'Kansas' : 'Topeka',
'Kentucky' : 'Frankfort',
'Louisiana' : 'Baton Rouge',
'Maine' : 'Augusta',
'Maryland' : 'Annapolis',
'Massachusetts' : 'Boston',
'Michigan' : 'Lansing',
'Minnesota' : 'Saint Paul',
'Mississippi' : 'Jackson',
'Missouri' : 'Jefferson City',
'Montana' : 'Helena',
'Nebraska' : 'Lincoln',
'Nevada' : 'Carson City',
'New Hampshire' : 'Concord',
'New Jersey' : 'Trenton',
'New Mexico' : 'Santa Fe',
'New York' : 'Albany',
'North Carolina' : 'Raleigh',
'North Dakota' : 'Bismarck',
'Ohio' : 'Columbus',
'Oklahoma' : 'Oklahoma City',
'Oregon' : 'Salem',
'Pennsylvania' : 'Harrisburg',
'Rhode Island' : 'Providence',
'South Carolina' : 'Columbia',
'South Dakota' : 'Pierre',
'Tennessee' : 'Nashville',
'Texas' : 'Austin',
'Utah' : 'Salt Lake City',
'Vermont' : 'Montpelier',
'Virginia' : 'Richmond',
'Washington' : 'Olympia',
'West Virginia' : 'Charleston',
'Wisconsin' : 'Madison',
'Wyoming' : 'Cheyenne',
}

print("~~~~~~STATE CAPITALS~~~~")
used = []
tally = []

def present_state():
  score = 0
  print(state)
  used.append(state)
  answer = input()
  if answer == capdic[state]:
    print("Correct!")
    score += 1 
    tally.append(score)
  else:
    print("Incorrect")
    print(f"The answer is: {capdic[state]}")
  total = sum(tally)
  print(f"Score: {total}")
  print("---------------------")

for states in capdic:
  state = random.choice(list(capdic))
  if state not in used:
    present_state()
  if state in used:
    state = random.choice(list(capdic))
    if state not in used:
      present_state()
  state = random.choice(list(capdic))
  if state not in used:
    present_state()
  if state in used:
    state = random.choice(list(capdic))
    if state not in used:
      present_state()
  state = random.choice(list(capdic))
  if state not in used:
    present_state()
  if state in used:
    state = random.choice(list(capdic))
    if state not in used:
      present_state()
 
total = sum(tally)
total_used = len(used)    
print(f"Congratulations. You scored {total}/{total_used}")
