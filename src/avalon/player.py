from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def newgame(n, role):
        pass
