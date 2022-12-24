class Node(object):

    def __init__(self, name: str):
        self.name: str = name
        self.neighbors: list = []

    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
