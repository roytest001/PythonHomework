from sys import exit
from random import randint
import room


ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod
}




room.runner(ROOMS, 'central_corridor')