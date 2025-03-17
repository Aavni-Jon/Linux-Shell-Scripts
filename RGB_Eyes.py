
from gpiozero import LED
from gpiozero import PWMLED
import time

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

# Raspberry Pi Pins
red_pwm_pin = PWMLED(3) 
green_pwm_pin = PWMLED(4) 
blue_pwm_pin = PWMLED(17) 

def eyes_RGB(eyes_status):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes_status)
    red,green,blue = eyes_status
    red_pwm_pin.value = eyes_status[red]
    green_pwm_pin.value = eyes_status[green]
    blue_pwm_pin.value = eyes_status[blue]

def main():
    #print("Welcome To The STEAM Clown Makey Bot")
    eyes_RGBLEDs = {'red_RGBLED':.1, 'green_RGBLED':.5, 'blue_RGBLED':.99}
    #eyes_RGBLEDs = {'left_eye':{'leye_red_RGBLED':1, 'leye_green_RGBLED':.5, 'leye_blue_RGBLED':.99}, 'right_eye':{'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.99}}
    if debug_messages : print("Calling eyes1_RGB function")
    eyes_RGB(eyes_RGBLEDs)
    if debug_messages : print("Returned from eyes_RGB function")

main()
