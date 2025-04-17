from djitellopy import Tello
import cv2

def basic_keyboard_control():
    tello = Tello()
    tello.connect()

    print("Battery:", tello.get_battery(), "%")

    tello.takeoff()
    print("Drone has taken off. Use keys to control:")
    print("w/a/s/d: move | q: land | esc: emergency stop")

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == ord('w'):
            tello.move_forward(30)
        elif key == ord('s'):
            tello.move_back(30)
        elif key == ord('a'):
            tello.move_left(30)
        elif key == ord('d'):
            tello.move_right(30)
        elif key == ord('q'):
            tello.land()
            break
        elif key == 27:  # ESC key
            tello.emergency()
            break

    tello.end()
