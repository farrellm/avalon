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
        print(self.roles)
        succeeded = 0
        failed = 0
        for mission in range(1, 5 + 1):
            print()
            print('mission', mission)
            self.turn = (self.turn + 1) % n
            m = self.proposal_size(mission)
            for vote in range(1, 5 + 1):
                print('vote', vote)

                prop = self.players[self.turn].get_proposal(m, mission, vote)
                assert m == len(prop)
                assert m == len(set(prop))
                print(prop)

                if vote < 4:
                    vs = [p.vote(prop, mission, vote) for p in self.players]
                    print(vs)
                    if sum(vs) >= math.ceil(n / 2):
                        break

            ss = [self.players[i].quest(prop, mission, vote) for i in prop]
            # ss.sort()
            print(ss)
            f = len([s for s in ss if not s])
            if f == 0 or (mission == 4 and f == 1):
                print('success')
                succeeded += 1
                for p in self.players:
                    p.success(mission, prop)
            else:
                print('failure')
                failed += 1
                for p in self.players:
                    p.failure(mission, prop)

            if failed >= 3:
                print('evil won')
                return False

            if succeeded >= 3:
                break

        print()
        for a in self.roles['assassin']:
            v = self.players[a].guess_merlin()
            print(v, 'assassinated')
            if v in self.roles['merlin']:
                print('merlin assassinated, evil won')
                return False

        print('good won')
        return True

    def newgame(self):
        n = len(self.players)

        self.roles = role.shuffle_roles(n)
        self.mission = 1
        self.vote = 1
        self.turn = random.randrange(n)

        for i in self.roles['merlin']:
            self.players[i].newgame(n, role.make_merlin(self.roles))
        for i in self.roles['percival']:
            self.players[i].newgame(n, role.make_percival(self.roles))
        for i in self.roles['loyal']:
            self.players[i].newgame(n, role.make_loyal(self.roles))
        for i in self.roles['mordred']:
            self.players[i].newgame(n, role.make_mordred(self.roles))
        for i in self.roles['morgana']:
            self.players[i].newgame(n, role.make_morgana(self.roles))
        for i in self.roles['assassin']:
            self.players[i].newgame(n, role.make_assassin(self.roles))
        for i in self.roles['minion']:
            self.players[i].newgame(n, role.make_minion(self.roles))

    _prop_1 = {1: 2, 2: 2, 3: 2, 4: 3, 5: 3}
    _prop_2 = {1: 2, 2: 3, 3: 3, 4: 4, 5: 4}
    _prop_3 = {1: 3, 2: 4, 3: 4, 4: 5, 5: 5}
    _proposal_size = {5: _prop_1,
                      6: _prop_2,
                      7: _prop_2,
                      8: _prop_3,
                      9: _prop_3,
                      10: _prop_3}

    def proposal_size(self, mission):
        return self._proposal_size[len(self.players)][mission]
