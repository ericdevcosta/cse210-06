
#This class should inherit action.py and polymorph the execute function

# from asteroids.casting.asteroid import asteroid
import constants
from asteroids.casting.actor import Actor
from asteroids.scripting.action import Action
from asteroids.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the Ship collides
    with the asteroid, or the beam collides with the asteroid, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_asteroid_collision(cast)
            self._handle_beam_collision(cast)
            self._handle_game_over(cast)

    def _handle_beam_collision(self, cast):
        """Updates the score and destroys the asteroid if the beam collides with the asteroid.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        asteroid = cast.get_first_actor("Asteroids")
        beam = cast.get_first_actor("Beams")
        asteroids = asteroid.get_segments()[0:]
        beams = beam.get_segments()[0:]

        for asteroid in asteroids:
            for beam in beams:
                if beam.get_position().equals(asteroid.get_position()):
                    points = asteroid.get_points()
                    score.add_points(points)
                    asteroid.reset()
                    beam.reset()
            
        
    
    def _handle_asteroid_collision(self, cast):
        """Sets the game over flag if the asteroid collides with the ship.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        ship = cast.get_first_actor("ship")
        asteroid = cast.get_first_actor("asteroids")
        score = cast.get_first_actor("scores")
        asteroids = cast.get_actors("asteroids")
        
        for asteroid in asteroids:
            if ship.get_position().equals(asteroid.get_position()):
                self._is_game_over = True
                score.add_points(25)
            
        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the ship and asteroid white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            score = cast.get_first_actor("scores").get_score()

            
            ship = cast.get_first_actor("Ships")
            asteroid = cast.get_first_actor("Asteroids")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("You have been Hit! , Your score is: ", score)
            message.set_position(position)
            cast.add_actor("messages", message)
            asteroids = asteroid.get_segments()[0:]


            for asteroid in asteroids:
                asteroid.set_color(constants.WHITE)
                
            ship.set_color(constants.WHITE)

        
            
