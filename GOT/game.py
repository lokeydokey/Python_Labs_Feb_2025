#! /usr/bin/env python3
# Author: Lverma
# Description: This is a game of Tanks
""" 
     GOT - Game of Tanks:
 
 """
import tank
import sys

def main():
    # Instantiate/Create 3 Tank objects
    erik_tank = tank.Tank("german", "tiger")
    zane_tank = tank.Tank("ameircan", "sherman")
    aram_tank = tank.Tank("british", "churchill")

    # And the game beings

    erik_tank.accel(61)
    zane_tank.accel(44)

    aram_tank.rotate_left(289)
    aram_tank.accel(31)
    aram_tank.shoot()

    # ...and success!
    erik_tank.take_damage(37)
    zane_tank.take_damage(49)

    # And now for some visuals....

    print(f"Health of Erik's tank is {erik_tank._health}")

    print(f"Status of Erik's and Zane's tank is {erik_tank + zane_tank}")

    # Erik receives a HEALTH BOOST!
    erik_tank._health = 100
    print(f"New health of Erik's Tank is {erik_tank._health}")
    erik_tank.set_health(101)
    print(f"New health of Erik's Tanks is {erik_tank.get_health()}")
    print(f"Erik {erik_tank.tank_health}")
    print(f"Zane {zane_tank.tank_health}")
    print(f"Aram {aram_tank.tank_health}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

