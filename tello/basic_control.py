from djitellopy import Tello
import time

def basic_takeoff_land():
    tello = Tello()
    tello.connect()

    print("Battery:", tello.get_battery())

    tello.takeoff()
    time.sleep(3)
    tello.land()
