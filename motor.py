from gpiozero import PWMOutputDevice
from time import sleep

pwm = PWMOutputDevice(4)
while True:
  pwm.on()
  sleep(1)
  pwm.off()
  sleep(1)
  pwm.value = 0.5
  sleep(1)
  pwm.value = 0.0
  sleep(1)
