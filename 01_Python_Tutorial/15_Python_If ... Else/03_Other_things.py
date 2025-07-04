
# >>>>> AND <<<<< # :
''' The and keyword is a logical operator, and is used to 
combine conditional statements: '''

''' Test if a is greater than b, AND if c is greater than a: '''
a = 200
b = 33
c = 500
if a > b and c > a: 
  print("Both conditions are True") # Output: Both codition are True



# >>>>> OR <<<<< # :
''' The or keyword is a logical operator, and is used to 
combine conditional statements: '''

''' Test if a is greater than b, OR if a is greater than c: '''
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") # Output: At least one of the condition is True



# >>>>> NOT <<<<< # :
''' The not keyword is a logical operator, and is used to 
reverse the result of the conditional statement: '''

a = 33
b = 200
if not a > b: # This will return True so code will executed
  print("a is NOT greater than b") # Output: a is NOT greater than b



# >>>>> NESTED IF <<<<< # :
''' You can have if statements inside if statements, this is 
called nested if statements. '''

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:    
    print("and also above 20!")
  else:
    print("but not above 20.")



# >>>>> THE PASS STATEMENT <<<<< # :
''' if statements cannot be empty, but if you for some reason have an 
if statement with no content, put in the pass statement to avoid 
getting an error. '''

a = 33
b = 200

if b < a:
  pass
else: 
   print("We passed is statement")
# If b < a, the program does nothing due to pass. Otherwise, it prints a message.
