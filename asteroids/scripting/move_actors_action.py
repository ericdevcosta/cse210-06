
#This class should inherit action.py and polymorph the execute function

from asteroids.scripting.action import Action

class MoveActorsAction(Action):

    def execute(self, cast, script):
        
        actors = cast.get_all_actors()
        
        ship = cast.get_first_actor("ships")

        for actor in actors:
            velocity = actor.get_velocity()
            actor.move_next(velocity)
            