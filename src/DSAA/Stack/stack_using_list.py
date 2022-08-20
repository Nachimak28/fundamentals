from typing import Optional
from abc import ABC, abstractmethod

class AbstractDataType(ABC):
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def pop_all(self):
        pass



class Stack(AbstractDataType):
    def __init__(self, max_size: Optional[int]=None) -> None:
        """
        Implementation of the Stack data structure using a list wrapped in a class

        Parameters
        ----------
        max_size : int/None
            Maximum size of the stack predefined (in case needed)

        Returns
        -------
        None
        """

        self.max_size = max_size
        self.data = []         # list as a stack

    def push(self, element):
        """
        Pushes an element to the top of stack - Last In
        Time complexity: Amortized O(1)
        """
        if self.is_full() == False:
            self.data.append(element)
        else:
            print('Stack is full, cannot add element')
    
    def pop(self):
        """
        Pops an element from the top of stack - Last In First Out
        Time complexity: Amortized O(1)
        """
        if self.is_empty() == False:
            return self.data.pop(-1)
        else:
            print('Stack is empty, nothing to pop')
    
    def peek(self):
        """
        Returns the top element of a stack without popping it
        Time complexity: O(1)
        """
        if self.is_empty() == False:
            return self.data[-1]
        else:
            print('Stack empty')
    
    def is_empty(self):
        """
        Checks if stack is empty
        Time complexity: O(1)
        """
        return len(self.data) == 0
    
    def is_full(self):
        """
        Checks if stack is full - Only works if max_size is defined during initialization
        Time complexity: O(1)
        """
        if self.max_size != None:
            return len(self.data) == self.max_size
        return False
    
    def size(self):
        """
        Returns the size of the stack (number of elements)
        Time complexity: O(1)
        """
        return len(self.data)

    def pop_all(self):
        """
        Clears stack by popping all elements
        Time complexity: O(n)
        """
        while self.data:
            self.pop()
    
    def __repr__(self):
        repr_string = ''
        if self.is_empty() == True:
            repr_string = 'Empty Stack'
        else:
            for i in self.data[::-1]:
                repr_string += f'{i} \n-----\n'
        return repr_string

# Example 1
stack = Stack()
print(stack)

##### push elements and print
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print('Size of stack ', stack.size())
# print(stack)

##### pop elements and print
# stack.pop()
# stack.pop()
# stack.pop()
print('Size of stack ', stack.size())
print(stack)

##### peek element
top = stack.peek()
print('Top ', top)
print('Size of stack ', stack.size())


##### Check if empty
print('Is the stack empty? -> ', stack.is_empty())
stack.pop_all()
print('Is the stack empty? -> ', stack.is_empty())
stack.pop()

##### Check for max size

stack_ms = Stack(max_size=5)

# push 4 elements
stack_ms.push(1)
stack_ms.push(2)
stack_ms.push(3)
stack_ms.push(4)

print('Is the stack full? -> ', stack_ms.is_full())
stack_ms.push(5)
print('Is the stack full? -> ', stack_ms.is_full())

stack_ms.push(6)
