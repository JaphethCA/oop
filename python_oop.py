from abc import ABCMeta, abstractmethod


# The Parent Class
class Animal(metaclass=ABCMeta):
    """
    Animal Abstract class
    """

    """
    # Abstraction is the process of hiding how an object works,
    # and showing the information of an object in understandable manner.
    # This parent class holds the common methods of how the properties are set
    # and so the user of the class does not need to know the exact details and
    # can simply use the class
    """
    @abstractmethod
    def __init__(self, name, breed, **kwargs):
        self.__name = name
        self.__breed = breed

    """
    # ** Encapsulation ** is a technique used to protect the information in an
    # object from another object.
    # In this case, the breed and name attributes cannot be directly accessed
    # by other objects. Instead, they are accessed through getters and setters
    """
    @property
    def breed(self):
        """
        :return:
        :rtype:
        """
        return int(self.__breed)

    @breed.setter
    def breed(self, breed):
        self.__breed = int(breed)

    @property
    def name(self):
        """
        :return:
        :rtype:
        """
        return self.__name

    @name.setter
    def name(self, name):
        if name.islower() or not name.isupper():
            self.__name = ''.join(name.split()).title()
        else:
            self.__name = ''.join(name.split())

    @staticmethod
    def talk():
        print("Hello!")

"""
# Inheritance - Inheritance is a way of forming new classes using classes
# that have already been defined.
# The Dog class is formed using the Animal class. It therefore shares
# attributes and methods of the Animal class. It inherits those properties
"""

class Dog(Animal):

    def __init__(self, *args, **kwargs):
        Animal.__init__(*args, **kwargs)

    """
    # Polymorphism:  This is the process of using an operator or function in
    different ways for different data input. It is the ability to redefine
    methods for derived classes. In this case, the 'talk' method has been
    redefined by the derived class Dog. Instead of printing 'Hello' like in the
    parent class, it prints. Woof!
    """
    @staticmethod
    def talk():
        print("Woof!")


# The Cat class also inherits the Animal class
class Cat(Animal):
    """
    Cat child class inheriting from Animal class
    """
    """
    # Overloading: This allows the use of a single method name
    # but use it in more than one way to get different outcomes depending on
    # "context" (which is typically the type or number of arguments passed in)
    # In this case, the __init__ function has been overloaded. It can be called
    # as such: __init__(name, breed), or with the additional argument as such:
    # __init__(name, breed, {"average_purr_frequency":34})
    # Calling it the second way provides an extra argument, which chages the
    # value of the 'average_purr_frequecy' attribute
    """
    def __init__(self, *args, **kwargs):
        # Frequency in decibels
        self.average_purr_frequency = kwargs.pop(
			         'average_purr_frequency', 25)
        super(Cat, self).__init__(*args, **kwargs)

    @staticmethod
    def talk():
        print("Meow!")
