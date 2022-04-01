import random
import constants
from asteroids.casting.actor import Actor
from asteroids.shared.point import Point


class Asteroid(Actor):
    """
    Asteroids that fly through space.
    
    The responsibility of an asteroid is to select a random position and points that it's worth.
    Attributes:
        _points (int): The number of points the asteroid is worth.
    """
    def __init__(self):
        "Constructs a new asteroid."
        super().__init__()
        self._points = 0
        self.set_text("@@@\n@@@\n@@@")
        self.set_color(constants.RED)
        self.reset()
        self._segments = []
        
    def reset(self):
        """Selects a random position and points that the Asteroid is worth."""
        position_numbers = random.randint(4, 10)
        for i in range(position_numbers):
          self._points = random.randint(1, 8)
          x = random.randint(1, constants.COLUMNS - 1)
          y = random.randint(1, constants.ROWS - 1)
          position = Point(x, y)
          position = position.scale(constants.CELL_SIZE)
          segment = Actor()
          segment.set_position(position)
          segment.set_text("@@@\n@@@\n@@@")
          segment.set_color(constants.RED)
          #self._segments.append(segment)
          self.set_position(position)

    def get_segments(self):
        return self._segments
        
    def get_points(self):
        """Gets the points the asteroid is worth.
        
        Returns:
            points (int): The points the asteroid is worth.
        """
        return self._points