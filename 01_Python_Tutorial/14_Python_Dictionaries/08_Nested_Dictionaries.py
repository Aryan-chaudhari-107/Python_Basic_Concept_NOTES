 
# >>>>> NESTED DICTIONARIES <<<<< # :
''' A dictionary can contain dictionaries, this is called nested dictionaries. '''

myfamily = {
    
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },

  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },

  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
  
}
print(myfamily)

''' Or, if you want to add three dictionaries into a new dictionary: '''

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


# >>>>> ACCESS ITEMS IN NESTED DICTIONARIES <<<<< # :
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"]) # Output: Tobias



# >>>>> LOOPING THROUGH NESTED DICTIONARIES <<<<< # :
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y]) # print(y, obj[y])
