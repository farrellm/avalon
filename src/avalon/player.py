from abc import ABC, abstractmethod
import random


class Player(ABC):
    @abstractmethod
    def newgame(self, n, role):
        pass

    @abstractmethod
    def get_proposal(self, m, mission, vote):
        pass

    @abstractmethod
    def vote(self, prop, mission, vote):
        pass

    @abstractmethod
    def quest(self, prop, mission, vote):
        pass

    @abstractmethod
    def success(self, mission, prop):
        pass

    @abstractmethod
    def failure(self, mission, prop):
        pass

    @abstractmethod
    def guess_merlin(self):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.n = 0
        self.role = None

    def newgame(self, n, role):
        self.n = n
        self.role = role

    def get_proposal(self, m, mission, vote):
        return random.sample(range(self.n), m)

    def vote(self, prop, mission, vote):
        return random.choice([True, False])

    def quest(self, prop, mission, vote):
        if self.role['is_good']:
            return True
        return random.choice([True, False])

    def success(self, mission, prop):
        pass

    def failure(self, mission, prop):
        pass

    def guess_merlin(self):
        return random.choice(list(set(range(self.n)) - self.role['evils']))
