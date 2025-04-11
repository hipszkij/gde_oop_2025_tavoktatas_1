from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def assemble(self):
        pass
