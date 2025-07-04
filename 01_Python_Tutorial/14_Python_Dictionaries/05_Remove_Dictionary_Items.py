
# >>>>> POP() METHOD <<<<< # :
''' The pop() method removes the item with the specified key name: '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) # Output: {'brand': 'Ford', 'year': 1964}



# >>>>> POPITEM() METHOD <<<<< # :
''' The popitem() method removes the last inserted item 
(in versions before 3.7, a random item is removed instead): '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang'}



# >>>>> DEL() METHOD <<<<< # :
''' The del keyword removes the item with the specified key name: '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) # Output: {'brand': 'Ford', 'year': 1964}

''' The del keyword can also delete the dictionary completely: '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.



# >>>>> CLEAR() METHOD <<<<< # :
''' The clear() method empties the dictionary: '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) # Output: {}