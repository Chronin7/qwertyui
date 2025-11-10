import pygame
def init_controller():
	pygame.joystick.init()
	joysticks = []
	for i in range(pygame.joystick.get_count()):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()
		joysticks.append(joystick)
		print(f"Detected joystick: {joystick.get_name()} (ID: {joystick.get_id()})")
	return joysticks
def get_controler_states(joysticks):
	states = {}
	for joystick in joysticks:
		joy_id = joystick.get_id()
		states[joy_id] = {
			'buttons': {i: joystick.get_button(i) for i in range(joystick.get_numbuttons())},
			'axes': {i: joystick.get_axis(i) for i in range(joystick.get_numaxes())},
			'hats': {i: joystick.get_hat(i) for i in range(joystick.get_numhats())}
		}
	#
	return states