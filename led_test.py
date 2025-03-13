#
import gpiozero
from gpiozero import LED
import time

blink_led = LED(3)
#GPIO.setmode(GPIO.BOARD) # Note This is specifying the physical pins on the Raspberry Pi Header 
#GPIO.setwarnings(False)
#GPIO.setup(blink_led,GPIO.OUT)
print(dir("LED"))
print(dir(LED))

while(True):
  print("LED on")
  #GPIO.output(blink_led,GPIO.HIGH)
  blink_led.on()
  time.sleep(1)
  print("LED off")
  #GPIO.output(blink_led,GPIO.LOW)
  blink_led.off()
  time.sleep(1)
print('Done')
