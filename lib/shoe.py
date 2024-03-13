#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition='Grungy'):
        self.brand = brand
        self.size = size
        self.condition = condition

    def __repr__(self):
        return f'This is the {self.brand} of the night...'

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if type(size) == int and size > 0:
            self._size = size
        else:
            print('size must be an integer')
        

    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = 'New'

