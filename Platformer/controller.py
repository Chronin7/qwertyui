import pygame,os
import time
def init():
    pass
def get_status():
    pass
def end():
    pygame.joystick.quit()
    pygame.quit()
    os._exit(0)
    quit()
pygame.init()
pygame.joystick.init()


# Initialize all detected joysticks
for i in range(pygame.joystick.get_count()):
	pygame.joystick.Joystick(i).init()

print(f"Detected {pygame.joystick.get_count()} joystick(s).")
for i in range(pygame.joystick.get_count()):
	print(f"Joystick {i}: {pygame.joystick.Joystick(i).get_name()}")
#init butttons
while True:
	# Process events to keep input states updated
	pygame.event.pump()
	# Read joystick states
	for i in range(pygame.joystick.get_count()):
		joystick = pygame.joystick.Joystick(i)
		axes = [round(joystick.get_axis(a),3) for a in range(joystick.get_numaxes())]
		buttons = [round(joystick.get_button(b),3) for b in range(joystick.get_numbuttons())]
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f"axes: {axes}")
		print(f"buttons: {buttons}")

	
