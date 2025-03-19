from gpiozero import LED
from gpiozero import PWMLED
import time

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

# Raspberry Pi Pins left eye
redleft_pwm_pin = PWMLED(3)
greenleft_pwm_pin = PWMLED(12)
blueleft_pwm_pin = PWMLED(13)
#Rasberry Pi Pind rigth eye
redrigth_pwm_pin = PWMLED(16)
greenrigth_pwm_pin = PWMLED(20)
bluerigth_pwm_pin = PWMLED(21)

def eyes_left_RGB(eyes_left):
    if debug_messages : print("Running lefteye_RGB function")
    if debug_messages : print(eyes_left)
    red,green,blue = eyes_left
    redleft_pwm_pin.value = eyes_left[red]
    greenleft_pwm_pin.value = eyes_left[green]
    blueleft_pwm_pin.value = eyes_left[blue]

def eyes_rigth_RGB(eyes_rigth):
    if debug_messages : print("Running rigtheye_RGB function")
    if debug_messages : print(eyes_rigth)
    red,green,blue = eyes_rigth
    redrigth_pwm_pin.value = eyes_rigth[red]
    greenrigth_pwm_pin.value = eyes_rigth[green]
    bluerigth_pwm_pin.value = eyes_rigth[blue]
def main():
    print("Welcome To The STEAM Clown Makey Bot")
    eyes_left_RGBLEDs = {'red_RGBLED':.4, 'green_RGBLED':.5, 'blue_RGBLED':0}
    #eyes_RGBLEDs = {'left_eye':{'leye_red_RGBLED':1, 'leye_green_RGBLED':.5, 'leye_blue_RGBLED':.99}, 'right_eye':{'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.99}}
    if debug_messages : print("Calling eyes_RGB function")
    eyes_left_RGB(eyes_left_RGBLEDs)
   
    eyes_rigth_RGBLEDs = {'red_RGBLED':.4, 'green_RGBLED':.5, 'blue_RGBLED':0}
    #eyes_RGBLEDs = {'rigth_eye':{'leye_red_RGBLED':1, 'leye_green_RGBLED':.5, 'leye_blue_RGBLED':.99}, 'right_eye':{'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.99}}
    if debug_messages : print("Calling eyes_RGB function")
    eyes_rigth_RGB(eyes_rigth_RGBLEDs)
   
    if debug_messages : print("Returned from eyes_RGB function")

main()
