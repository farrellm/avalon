from enum import Enum, auto
import random


class Role(Enum):
    MERLIN = auto()
    PERCIVAL = auto()
    LOYAL = auto()
    MORDRED = auto()
    MORGANA = auto()
    ASSASSIN = auto()
    MINION = auto()


def shuffle_roles(n):
    rp = list(range(n))
    random.shuffle(rp)
    if n == 5:
        return dict(mordred=(rp[0],),
                    morgana=(),
                    assassin=(rp[1],),
                    minion=(),
                    merlin=(rp[2],),
                    percival=(),
                    loyal=(rp[3], rp[4]))
    if n == 6:
        return dict(mordred=(rp[0],),
                    morgana=(),
                    assassin=(rp[1],),
                    minion=(),
                    merlin=(rp[2],),
                    percival=(),
                    loyal=(rp[3], rp[4], rp[5]))
    if n == 7:
        return dict(mordred=(rp[0],),
                    morgana=(rp[1]),
                    assassin=(rp[2],),
                    minion=(),
                    merlin=(rp[3],),
                    percival=(rp[4]),
                    loyal=(rp[5], rp[6]))
    if n == 8:
        return dict(mordred=(rp[0],),
                    morgana=(rp[1]),
                    assassin=(rp[2],),
                    minion=(),
                    merlin=(rp[3],),
                    percival=(rp[4]),
                    loyal=(rp[5], rp[6], rp[7]))
    if n == 9:
        return dict(mordred=(rp[0],),
                    morgana=(rp[1]),
                    assassin=(rp[2],),
                    minion=(),
                    merlin=(rp[3],),
                    percival=(rp[4]),
                    loyal=(rp[5], rp[6], rp[7], rp[8]))
    if n == 10:
        return dict(mordred=(rp[0],),
                    morgana=(rp[1]),
                    assassin=(rp[2],),
                    minion=(rp[3]),
                    merlin=(rp[4],),
                    percival=(rp[5]),
                    loyal=(rp[6], rp[7], rp[8], rp[9]))


def evil_evils(roles):
    return set(roles['mordred'] +
               roles['morgana'] +
               roles['assassin'] +
               roles['minion'])


def make_merlin(roles):
    return dict(role=Role.MERLIN,
                is_good=True,
                evils=(roles['morgana'] +
                       roles['assassin'] +
                       roles['minion']),
                merlins=())


def make_percival(roles):
    return dict(role=Role.PERCIVAL,
                is_good=True,
                evils=(),
                merlins=(roles['merlin'] +
                         roles['morgana']))


def make_loyal(roles):
    return dict(role=Role.LOYAL,
                is_good=True,
                evils=(),
                merlins=())


def make_mordred(roles):
    return dict(role=Role.MORDRED,
                is_good=False,
                evils=evil_evils(roles),
                merlins=())


def make_morgana(roles):
    return dict(role=Role.MORGANA,
                is_good=False,
                evils=evil_evils(roles),
                merlins=())


def make_assassin(roles):
    return dict(role=Role.ASSASSIN,
                is_good=False,
                evils=evil_evils(roles),
                merlins=())


def make_minion(roles):
    return dict(role=Role.MINION,
                is_good=False,
                evils=evil_evils(roles),
                merlins=())
