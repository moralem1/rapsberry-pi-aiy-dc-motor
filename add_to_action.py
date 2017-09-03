# =========================================
# Makers! Implement your own actions here.
# =========================================

from gpiozero import PWMOutputDevice

class MotorMove(object):
  def __init__(self):
    self.pwm = PWMOutputDevice(4)

  def run(self, voice_command):
    if 'on' in voice_command:
      self.pwm.on()
    elif 'off' in voice_command:
      self.pwm.off()

  # =========================================
  # Makers! Add your own voice commands here.
  # =========================================
  actor.add_keyword('motor', MotorMove())
    
  return actor
