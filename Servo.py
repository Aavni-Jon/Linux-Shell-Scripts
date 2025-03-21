from gpiozero import Servo
from time import sleep

servo = Servo(18)

try:
    while True:
        servo.min()  # Indented to be inside the while loop
        sleep(0.5)
        servo.mid()  # Indented to be inside the while loop
        sleep(0.5)
        servo.max()  # Indented to be inside the while loop
        sleep(0.5)
except KeyboardInterrupt:
    print("Program stopped")
