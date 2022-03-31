
#This class should inherit action.py and polymorph the execute function

from asteroids.scripting.action import Action

class MoveActorsAction(Action):

    def execute(self, cast, script):
        
        actors = cast.get_all_actors()

        for actor in actors:
            actor.move_next()
            