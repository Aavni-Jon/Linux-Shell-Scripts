# GitHub: https://github.com/Aavni-Jon/Linux-Shell-Scripts/blob/main/White_LED-code.py
# Program/Design Name:    Traffic_LED-code.py
# Description:    This is a program to use a dictionary to turn on an LED
# based on a set of 3 values found in a "traffic_light" dictionary
# Program description:
# 1) Import libraries and set LED pin
# 2) Create a dictionary containing values for the "traffic light" LEDs
# 3) Print and Light "traffic light" LEDs based on provided values
# Dependencies:   python3
#   Inputs: traffic_status to set "traffic_light" LEDs
#   Outputs: Welcome message, light  status, and value of red_LED
# Revision:
#  Revision 0.03 - Updated 03/14/2025 added blink code
#  Revision 0.02 - Updated 03/13/2025 changed variable names, added conditionals for all LEDs
#  Revision 0.01 - Created 03/12/2025
import gpiozero
from gpiozero import LED
import time

red_LED = LED(3) #Using BCM GPIO3 on Board pin 5
yellow_LED = LED(27) #Using BCM GPIO27 on Board pin 13 
green_LED = LED(10) #Using BCM GPIO10 on Board pin 19

def stop_light(traffic_status):
    print(traffic_status)
    red, yellow, green = traffic_status
    #red_LED status
    print(traffic_status[red])
    if(traffic_status[red]):
        red_LED.on()
    else:
        red_LED.off()
    #yellow_LED status
    print(traffic_status[yellow])
    if(traffic_status[yellow]):
        yellow_LED.on()
    else:
        yellow_LED.off()
    #green_LED status
    print(traffic_status[green])
    if(traffic_status[green]):
        green_LED.on()
    else:
        green_LED.off()
   
def main():
    print("Welcome to the STEAM Clown Makey Bot")
    traffic_light = {'red_LED': 1, 'yellow_LED': 1,'green_LED': 1}
    stop_light(traffic_light)
    while(traffic_light):
        red_LED.on()
        time.sleep(0.1)
        yellow_LED.on()
        time.sleep(0.1)
        green_LED.on()
        time.sleep(0.1)
        red_LED.off()
        time.sleep(0.1)
        yellow_LED.off()
        time.sleep(0.1)
        green_LED.off()
        time.sleep(0.1)
   
main()
