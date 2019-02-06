import sys

from avalon.game import Game
from avalon.player import RandomPlayer


def main():
    ps = [RandomPlayer() for i in range(5)]
    g = Game(ps)
    g.run()
    print()
    print(g.roles)

    return 0


if __name__ == '__main__':
    sys.exit(main())
