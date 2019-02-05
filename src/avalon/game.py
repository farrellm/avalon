import math
import random

import avalon.role as role


class Game:
    def __init__(self, players):
        self.players = players
        self.roles = dict()
        self.mission = 0
        self.vote = 0
        self.turn = -1

    def run(self):
        n = len(self.players)
        self.newgame()
        failed = 0
        for mission in range(5):
            m = self.proposal_size(n, mission)
            for vote in range(5):
                prop = self.players.get_proposal(m, mission, vote)
                assert m == len(prop)
                assert m == len(set(prop))
                if vote < 4:
                    vs = [p.vote(prop, mission, vote) for p in self.players]
                    if sum(vs) > math.ceil(n / 2):
                        break
            ss = [self.players[i].quest(prop, mission, vote) for i in prop]
            f = len(s for s in ss if not s)
            if f == 0 or (mission == 1 and f == 1):
                for p in self.players:
                    p.success(mission, prop)
            else:
                failed += 1
                for p in self.players:
                    p.success(mission, prop)
        if failed >= 3:
            return False
        evils = (self.roles.mordred +
                 self.roles.morgana +
                 self.roles.minion)
        for a in self.roles.assassin:
            for p in evils:
                a.listen_merlin(p.suggest_merlin())
        if a.suggest_merlin() in self.roles.merlin:
            return False
        return True

    def newgame(self):
        n = len(self.players)

        self.roles = role.shuffle_roles()
        self.mission = 1
        self.vote = 1
        self.turn = random.randrange(n)

        for i in self.roles.merlin:
            self.players[i].newgame(n, role.make_merlin(self.roles))
        for i in self.roles.percival:
            self.players[i].newgame(n, role.make_percival(self.roles))
        for i in self.roles.loyal:
            self.players[i].newgame(n, role.make_loyal(self.roles))
        for i in self.roles.mordred:
            self.players[i].newgame(n, role.make_mordred(self.roles))
        for i in self.roles.morgana:
            self.players[i].newgame(n, role.make_morgana(self.roles))
        for i in self.roles.assassin:
            self.players[i].newgame(n, role.make_assassin(self.roles))
        for i in self.roles.minion:
            self.players[i].newgame(n, role.make_minion(self.roles))
