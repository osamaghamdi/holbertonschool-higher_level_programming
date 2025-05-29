#!/usr/bin/env python3
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Method to be implemented by subclasses to return the sound of the animal."""
        pass
    
class Dog(Animal):
    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
