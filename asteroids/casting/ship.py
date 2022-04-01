import constants
from asteroids.casting.actor import Actor
from asteroids.shared.point import Point

class Ship(Actor):
    """
    
    
    The responsibility of ship is to move itself and shoot beams.

    Attributes:
        _points (int): The number of points for destroing asteroids.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self, velocity):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def _prepare_body(self):
         
        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SHIP_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "🚀" 
            color = constants.YELLOW 
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
            
    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)