from abc import ABC, abstractmethod
from typing import Optional
from queue import LifoQueue

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
        self.max_size = max_size if max_size != None else 0
        self.data = LifoQueue(maxsize=self.max_size)

    def push(self, element):
        if self.is_full() == False:
            self.data.put(element)
        else:
            print('Stack is full, cannot add element')

    def pop(self):
        if self.is_empty() == False:
            return self.data.get_nowait()
        else:
            print('Stack is empty, nothing to pop')

    def peek(self):
        print('Peek Not available')

    def is_empty(self):
        return self.data.empty()

    def is_full(self):
        return self.data.full()

    def size(self):
        return self.data.qsize()

    def pop_all(self):
        while self.is_empty() == False:
            self.data.get_nowait()
        

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
   