import constants

from asteroids.casting.cast import Cast
from asteroids.casting.beam import Beam
#from asteroids.casting.score import Score
from asteroids.casting.ship import Ship
from asteroids.casting.asteroid import Asteroid
from asteroids.scripting.script import Script
from asteroids.scripting.control_ship_action import ControlActorsAction
from asteroids.scripting.move_actors_action import MoveActorsAction
from asteroids.scripting.handle_collisions_action import HandleCollisionsAction
from asteroids.scripting.draw_actors_action import DrawActorsAction
from asteroids.director import Director
from asteroids.services.keyboard_service import KeyboardService
from asteroids.services.video_service import VideoService
from asteroids.shared.color import Color
from asteroids.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("beams", Beam())
    cast.add_actor("ships", Ship())
    #cast.add_actor("scores", Score("player1"))
    cast.add_actor("asteroids", Asteroid())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()