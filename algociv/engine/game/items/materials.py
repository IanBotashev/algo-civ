class Material:
    __name__ = None
    __description__ = None

    # The amount of energy given after put into the Generator module.
    __energy__ = None


class Stone(Material):
    __name__ = 'Stone'
    __description__ = 'Stone'
    __energy__ = 10


class Dirt(Material):
    __name__ = 'Dirt'
    __description__ = 'Dirt. This is dirt. I think this is dirt?'
    __energy__ = 1
