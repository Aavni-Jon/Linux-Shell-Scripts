from gpiozero import RGBLED
import time

led = RGBLED(red=3, green=12, blue=13)

def stop_light(traffic_status):

    red_value, green_value, yellow_value = traffic_status
   
    # the traffic light sequence
    print("Green LED ON")
    led.color = (0, 1, 1)  # ( 0 = off, 1 = on)
    time.sleep(3)
   
    print("Yellow LED ON")
    led.color = (0.6, 0.7,0)  #  (Red + Green = Yellow)
    time.sleep(2)

    print("Red LED ON")
    led.color = (1, 0, 0)  #  ( 0 = off, 1 = on)
    time.sleep(4)


def main():
    while True:
        # order
        traffic_light = (1, 1, 0)  # Red, Green, Yellow

        # Call the stop_light function with the traffic light configuration
        stop_light(traffic_light)

if __name__ == "__main__":
    main()
