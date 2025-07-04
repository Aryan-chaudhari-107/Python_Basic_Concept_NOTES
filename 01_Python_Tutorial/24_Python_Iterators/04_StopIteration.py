
'''  
The example in (03) would continue forever if you had enough next() statements, or if 
it was used in a for loop.

To prevent the iteration from going on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the 
iteration is done a specified number of times:
'''

class mynum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration
    
myclass = mynum()
myiter = iter(myclass)

for x in myiter:
    print(x)