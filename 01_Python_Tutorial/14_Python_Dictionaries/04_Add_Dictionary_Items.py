
# >>>>> ADDING ITEMS <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}



# >>>>> UPDATE DICTIONARY <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}