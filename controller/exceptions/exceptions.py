class PersonNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Person not found")

class HouseNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "House not found")