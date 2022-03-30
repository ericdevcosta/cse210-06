import constants
from asteroids.casting.actor import Actor
from asteroids.shared.point import Point

class ship(Actor):
    """
    
    
    The responsibility of ship is to move itself and shoot asteroids.

    Attributes:
        _points (int): The number of points for destroing asteroids.
    """
    def __init__(self):
        super().__init__()

    def turn_ship(self, velocity):
        pass

    def move_ship(self, velocity):
        pass

    def shoot_beam(self,velocity):
        pass