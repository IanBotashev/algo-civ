class Material:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __repr__(self):
        return f"<Material(name: {self.__class__.__name__}, kwargs: {self.kwargs})>"


class Coal(Material):
    pass
