'''
handles all the obstacles from walls to houses.
Where the avatar can go, what kind of behavior it should have
'''
class Obstacle:
    def __init__(self, cord: tuple, area: int) -> None:
        self.x_pos, self.y_pos = cord
        self.area = area

    def get_cord(self) -> tuple:
        return (self.x_pos, self.y_pos)

    def get_area(self) -> int:
        return self.area


class Wall(Obstacle):
    pass


class Door(Obstacle):
    pass


class Grass(Obstacle):
    pass


class Water(Obstacle):
    pass


class Cliff(Obstacle):
    pass