from gpiozero import LED
from gpiozero import PWMLED
import time

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

# Raspberry Pi Pins
led_pwm_pin = PWMLED(3) 
 
def led_RGB(brightness):
    if debug_messages : print("Running led_RGB function")
    if debug_messages : print(brightness)
    led_pwm_pin.value = brightness
    
def main():
    print("Welcome To The STEAM Clown Makey Bot")
    while(True):
        user_RGB_value = float(input("Enter a number from 0-1, so 0, .42, .82, or 1 is OK > "))
        if debug_messages : print("Calling led_RGB function")
        led_RGB(user_RGB_value)
        if debug_messages : print("Returned from led_RGB function")

main()
