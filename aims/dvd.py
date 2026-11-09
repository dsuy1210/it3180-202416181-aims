class DigitalVideoDisc:
    """Represents a DVD in the AIMS store."""

    def __init__(self, title, category=None, director=None, length=None, cost=0.0):
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = cost

    def __str__(self):
        return f"DVD - {self.title} - {self.category} - {self.director} - {self.length} min: {self.cost} $"
