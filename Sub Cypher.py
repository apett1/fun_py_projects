#Cyphers words into a number code and decyphers back to words

dict_rev = {
  "61" : "a",
  "611" : "A",
  "22" : "b",
  "221" : "B",
  "4" : "c",
  "41" : "C",
  "25" : "d",
  "251" : "D",
  "79" : "e",
  "791" : "E",
  "85" : "f",
  "851" : "F",
  "19" : "g",
  "191" : "G",
  "21" : "h",
  "211" : "H",
  "43" : "i",
  "431" : "I",
  "59" : "j",
  "591" : "J",
  "54" : "k",
  "541" : "K",
  "67" : "l",
  "671" : "L",
  "81" : "m",
  "811" : "M",
  "16" : "n",
  "161" : "N",
  "0" : "o",
  "11" : "O",
  "17" : "p",
  "171" : "P",
  "5" : "q",
  "51" : "Q",
  "76" : "r",
  "761" : "R",
  "35" : "s",
  "351" : "S",
  "97" : "t",
  "971" : "T",
  "70" : "u",
  "701" : "U",
  "50" : "v",
  "50.1" : "V",
  "86" : "w",
  "861" : "W",
  "65" : "x",
  "651" : "X",
  "38" : "y",
  "381" : "Y",
  "37" : "z",
  "371" : "Z",
  "69" : " "
}

dict = {
  "a" : 61,
  "A" : 611,
  "b" : 22,
  "B" : 221,
  "c" : 4,
  "C" : 41,
  "d" : 25,
  "D" : 251,
  "e" : 79,
  "E" : 791,
  "f" : 85,
  "F" : 851,
  "g" : 19,
  "G" : 191,
  "h" : 21,
  "H" : 211,
  "i" : 43,
  "I" : 431,
  "j" : 59,
  "J" : 591,
  "k" : 54,
  "K" : 541,
  "l" : 67,
  "L" : 671,
  "m" : 81,
  "M" : 811,
  "n" : 16,
  "N" : 161,
  "o" : 0,
  "O" : 11,
  "p" : 17,
  "P" : 171,
  "q" : 5,
  "Q" : 51,
  "r" : 76,
  "R" : 761,
  "s" : 35,
  "S" : 351,
  "t" : 97,
  "T" : 971,
  "u" : 70,
  "U" : 701,
  "v" : 50,
  "V" : 501,
  "w" : 86,
  "W" : 861,
  "x" : 65,
  "X" : 651,
  "y" : 38,
  "Y" : 381,
  "z" : 37,
  "Z" : 371,
  " " : 69
}

print("Cypher or Decypher?")
choice = input()
choice = choice.title()
if choice == "Cypher":
  print("Enter word or phrase to be cyphered (alpha only, no special char)")
  word = input()
  def split(word):
    return [char for char in word]
  letters = split(word)
  value_list = []
  for letter in letters:
    values = dict.get(letter)
    values = str(values)
    value_list.append(values)
    output = ' '.join(value_list)
  print(output)

if choice == "Decypher":
  print("Enter numbers to be decyphered, separated by a space")
  numbers = input()
  numbers_list = numbers.split()
  value_list = []
  for number in numbers_list:
    values = dict_rev.get(number)
    value_list.append(values)
  output = ''.join(value_list)
  print(output)