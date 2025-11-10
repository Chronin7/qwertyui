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
	# This function is used by your main file to get the simple {'left': True/False, ...} state
	
	# 1. Get the current state of all keyboard keys
	keys = pygame.key.get_pressed()
	
	# 2. Initialize the required state dictionary with keyboard inputs
	state = {
		'left': keys[pygame.K_LEFT] or keys[pygame.K_a],
		'right': keys[pygame.K_RIGHT] or keys[pygame.K_d],
		'up': keys[pygame.K_UP] or keys[pygame.K_w],
		'down': keys[pygame.K_DOWN] or keys[pygame.K_s],
		'jump': keys[pygame.K_SPACE],
	}
	
	# 3. Overlay joystick input (if any)
	for joystick in joysticks:
		# Check Hats (D-Pads)
		if joystick.get_numhats() > 0:
			hat = joystick.get_hat(0)
			if hat[0] == -1: state['left'] = True
			if hat[0] == 1: state['right'] = True
			if hat[1] == 1: state['up'] = True
			if hat[1] == -1: state['down'] = True
		
		# Check Axes (Analog Sticks)
		if joystick.get_numaxes() > 0:
			axis_x = joystick.get_axis(0)
			axis_y = joystick.get_axis(1)
			if axis_x < -0.5: state['left'] = True
			if axis_x > 0.5: state['right'] = True
			if axis_y < -0.5: state['up'] = True
			if axis_y > 0.5: state['down'] = True
			
		# Check Buttons (example for jump on button 0)
		if joystick.get_numbuttons() > 0 and joystick.get_button(0):
			state['jump'] = True

	return state


# The secondary function for detailed key tracking (not used by your main file currently)
def get_unified_state(joysticks):
	keys = pygame.key.get_pressed()
	
	states = {
		"keyboard": {
			"`":keys[pygame.K_BACKQUOTE],"1":keys[pygame.K_1],"2":keys[pygame.K_2],"3":keys[pygame.K_3],
			"4":keys[pygame.K_4],"5":keys[pygame.K_5],"6":keys[pygame.K_6],"7":keys[pygame.K_7],
			"8":keys[pygame.K_8],"9":keys[pygame.K_9],"0":keys[pygame.K_0],"minus":keys[pygame.K_MINUS],
			"equals":keys[pygame.K_EQUALS],"backspace":keys[pygame.K_BACKSPACE],"tab":keys[pygame.K_TAB],
			"q":keys[pygame.K_q],"w":keys[pygame.K_w],"e":keys[pygame.K_e],"r":keys[pygame.K_r],
			"t":keys[pygame.K_t],"y":keys[pygame.K_y],"u":keys[pygame.K_u],"i":keys[pygame.K_i],
			"o":keys[pygame.K_o],"p":keys[pygame.K_p],"left_bracket":keys[pygame.K_LEFTBRACKET],
			"right_bracket":keys[pygame.K_RIGHTBRACKET],"enter":keys[pygame.K_RETURN],
			"left_ctrl":keys[pygame.K_LCTRL],"a":keys[pygame.K_a],"s":keys[pygame.K_s],
			"d":keys[pygame.K_d],"f":keys[pygame.K_f],"g":keys[pygame.K_g],"h":keys[pygame.K_h],
			"j":keys[pygame.K_j],"k":keys[pygame.K_k],"l":keys[pygame.K_l],"semicolon":keys[pygame.K_SEMICOLON],
			"apostrophe":keys[pygame.K_QUOTE],"left_shift":keys[pygame.K_LSHIFT],"backslash":keys[pygame.K_BACKSLASH],
			"z":keys[pygame.K_z],"x":keys[pygame.K_x],"c":keys[pygame.K_c],"v":keys[pygame.K_v],
			"b":keys[pygame.K_b],"n":keys[pygame.K_n],"m":keys[pygame.K_m],"comma":keys[pygame.K_COMMA],
			"period":keys[pygame.K_PERIOD],"slash":keys[pygame.K_SLASH],"right_shift":keys[pygame.K_RSHIFT],
			"left_alt":keys[pygame.K_LALT],"space":keys[pygame.K_SPACE],"right_alt":keys[pygame.K_RALT],
			"right_ctrl":keys[pygame.K_RCTRL],"up":keys[pygame.K_UP],"down":keys[pygame.K_DOWN],
			"left":keys[pygame.K_LEFT],"right":keys[pygame.K_RIGHT],"insert":keys[pygame.K_INSERT],
			"home":keys[pygame.K_HOME],"page_up":keys[pygame.K_PAGEUP],"delete":keys[pygame.K_DELETE],
			"end":keys[pygame.K_END],"page_down":keys[pygame.K_PAGEDOWN],"f1":keys[pygame.K_F1],
			"f2":keys[pygame.K_F2],"f3":keys[pygame.K_F3],"f4":keys[pygame.K_F4],"f5":keys[pygame.K_F5],
			"f6":keys[pygame.K_F6],"f7":keys[pygame.K_F7],"f8":keys[pygame.K_F8],"f9":keys[pygame.K_F9],
			"f10":keys[pygame.K_F10],"f11":keys[pygame.K_F11],"f12":keys[pygame.K_F12],"num_lock":keys[pygame.K_NUMLOCK],
			"keypad_divide":keys[pygame.K_KP_DIVIDE],"keypad_multiply":keys[pygame.K_KP_MULTIPLY],"keypad_minus":keys[pygame.K_KP_MINUS],
			"keypad_plus":keys[pygame.K_KP_PLUS],"keypad_enter":keys[pygame.K_KP_ENTER],"keypad_1":keys[pygame.K_KP1],
			"keypad_2":keys[pygame.K_KP2],"keypad_3":keys[pygame.K_KP3],"keypad_4":keys[pygame.K_KP4],
			"keypad_5":keys[pygame.K_KP5],"keypad_6":keys[pygame.K_KP6],"keypad_7":keys[pygame.K_KP7],
			"keypad_8":keys[pygame.K_KP8],"keypad_9":keys[pygame.K_KP9],"keypad_0":keys[pygame.K_KP0],
			"keypad_period":keys[pygame.K_KP_PERIOD],"escape":keys[pygame.K_ESCAPE],"caps_lock":keys[pygame.K_CAPSLOCK],
			"scroll_lock":keys[pygame.K_SCROLLLOCK],"pause":keys[pygame.K_PAUSE],"print_screen":keys[pygame.K_PRINTSCREEN],
			"left_meta":keys[pygame.K_LMETA],"right_meta":keys[pygame.K_RMETA],"menu":keys[pygame.K_MENU],
			"mousex":pygame.mouse.get_pos()[0],"mousey":pygame.mouse.get_pos()[1],
			"mouse_buttons":{"left":pygame.mouse.get_pressed()[0],"middle":pygame.mouse.get_pressed()[1],"right":pygame.mouse.get_pressed()[2],}
		},
		"controller": {
			# Default values for controller buttons/axes
		}
	}
	
	# 4. Populate controller states
	for joystick in joysticks:
		joy_id = joystick.get_id()
		states["controller"][joy_id] = {
			'buttons': {i: joystick.get_button(i) for i in range(joystick.get_numbuttons())},
			'axes': {i: joystick.get_axis(i) for i in range(joystick.get_numaxes())},
			'hats': {i: joystick.get_hat(i) for i in range(joystick.get_numhats())}
		}
	
	return states
	
if __name__ == "__main__":
	# --- Test logic for this file ---
	pygame.init()
	pygame.display.set_mode((640, 480))
	joysticks = init_controller()
	running = True
	while running:
		# You MUST process events in the main loop for input functions to work
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		# We test the function your main script actually uses:
		state = get_controler_states(joysticks) 
		
		# Simple print to verify keyboard input works
		if state['left']:
			print("Left is pressed")
		if state['right']:
			print("Right is pressed")
		if state['up']:
			print("Up is pressed")
		if state['down']:
			print("Down is pressed")
		if state['jump']:
			print("Jump is pressed")