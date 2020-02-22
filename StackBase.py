from abc import ABC, abstractmethod     #Abstract Base Class

class StackBase(ABC):
    """
    Base class for Stack ADT
    """

    @abstractmethod
    def getTop(self):
        """ Return the top item of stack. None if stack is empty."""
        pass

    @abstractmethod
    def push(self, newItem):
        """ Push (i.e. add) [newItem] on top of stack."""
        pass

    @abstractmethod
    def pop(self):
        """ Pop (i.e. pop) [newItem] from top of stack."""
        pass

    @abstractmethod
    def size(self):
        """ Return size of the Stack, i.e. number of items"""
        pass
    
    @abstractmethod
    def isEmpty(self):
        """ Return True if Stack is empty. False otherwise"""
        pass

def main():
    s = StackBase()

    #should fail as StackBase is an abstract class
    print(s.size())   
    print(s.isEmpty())


if __name__ == "__main__":
    main()
