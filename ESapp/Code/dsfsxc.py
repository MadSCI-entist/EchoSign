import serial
import keyboard
import pyttsx3


# Configure the serial connections
arduino1_port = "COM5"  # Replace with the actual COM port for Arduino 1
arduino2_port = "COM4"  # Replace with the actual COM port for Arduino 2
baud_rate = 9600

arduino1_serial = serial.Serial(arduino1_port, baud_rate)
arduino2_serial = serial.Serial(arduino2_port, baud_rate)

engine = pyttsx3.init()



# Initialize flags for each condition
condition_flags = {
    'A': False,
    'B': False,
    'C': False,
    'D': False,
    'E': False,
    'F': False,
    'G': False,
    'H': False,
	'Name is' : False,
	'Alfred' : False,
	'Team' : False,
	'we' : False,
	'EchoSign' : False,
	'Hello' : False
	}


while True:
			
		try:
			data1 = arduino1_serial.readline().decode().strip()
			data2 = arduino2_serial.readline().decode().strip()
			sensor_data1 = data1.split(",")
			sensor_data2 = data2.split(",")

			X1, Y1, Z1 , F1, F2, F3, F4, F5 = sensor_data1
			X2, Y2, Z2 , F6, F7, F8, F9, F10 = sensor_data2

			X1, Y1, Z1 , F1, F2, F3, F4, F5 = int(X1),int(Y1),int(Z1) ,int(F1) ,int(F2) ,int(F3) ,int(F4) ,int(F5) 
			X2, Y2, Z2 , F6, F7, F8, F9, F10 = int(X2),int(Y2),int(Z2) ,int(F6) ,int(F7) ,int(F8) ,int(F9) ,int(F10) 

			if F1 < 205 and F1 > 175 and F2 < 180 and F2 > 145 and F3 < 140 and F3 > 110 and F4 < 200 and F4 > 150 and F5 < 250 and F5 > 190 and not condition_flags ['A']:
				print('A')
				engine.say("A")
				engine.runAndWait()
				condition_flags['A'] = True
				condition_flags['B'] = False
				condition_flags['Hello'] = True

			if F5 == 0 and not condition_flags ['Hello']:
				print('hello, How are you?')
				engine.say("hello, How are you?")
				engine.runAndWait()
				condition_flags['Hello'] = True
				condition_flags['B'] = True


			elif F1 < 230 and F1 > 180 and F2 < 200 and F2 > 135 and F3 < 265 and F3 > 230 and F4 < 305 and F4 > 2765 and F5 < 225 and F5 > 180 and F6 < 250 and F6 > 180 and F7 < 320 and F7 > 280 and F8 < 285 and F8 > 260 and F9 < 235 and F9 > 160 and F10 < 200 and F10 > 160 and not condition_flags ['Name is']:
				print(' My Name is')
				engine.say(" My Name is")
				engine.runAndWait()
				condition_flags['Name is'] = True
				condition_flags['G'] = False
				condition_flags['Alfred'] = False

			elif  F6 < 230 and F6 > 185 and F7 < 230 and F7 > 200 and F8 < 200 and F8 > 160 and F9 < 200 and F9 > 175 and F10 < 190 and F10 > 160 and not condition_flags ['Alfred']:
				print('Alfred')
				engine.say("i AM ALFRE")
				engine.runAndWait()
				condition_flags['Alfred'] = True
				condition_flags['Name is'] = False

			elif  F6 < 215 and F6 > 185 and F7 < 320 and F7 > 280 and F8 < 300 and F8 > 270 and F9 < 305 and F9 > 260 and F10 < 255 and F10 > 200 and not condition_flags ['we']:
				print(' we are')
				engine.say("we are")
				engine.runAndWait()
				condition_flags['we'] = True
				condition_flags['and'] = False
				condition_flags ['F'] = True


			elif  F1 < 310 and F1 > 270 and F2 < 265 and F2 > 245 and F3 < 260 and F3 > 230 and F4 < 205 and F4 > 175 and F5 < 220 and F5 > 140 and F6 < 230 and F6 > 195 and F7 < 260 and F7 > 220 and F8 < 290 and F8 > 220 and F9 < 295 and F9 > 250 and F10 < 265 and F10 > 230 and not condition_flags ['Team']:
				print('Team')
				engine.say("Team")
				engine.runAndWait()
				condition_flags['Team'] = True
				condition_flags['we'] = False
				condition_flags [ 'Hello'] = False

				condition_flags ['EchoSign'] = False

			

			elif  F6 < 215 and F6 > 190 and F7 < 300 and F7 > 260 and F8 < 210 and F8 > 180 and F9 < 295 and F9 > 250 and F10 < 265 and F10 > 210 and not condition_flags ['EchoSign']:
				print('EchoSign')
				engine.say("EchoSign")
				engine.runAndWait()
				condition_flags['EchoSign'] = True
				condition_flags['Team'] = False
				


			elif F1 < 315 and F1 > 280 and F2 < 265 and F2 > 220 and F3 < 250 and F3 > 220 and F4 < 300 and F4 > 255 and F5 < 215 and F5 > 190 and not condition_flags ['B']:
				print('B')
				engine.say("B")
				engine.runAndWait()
				condition_flags['B'] = True
				condition_flags['A'] = False
								

			elif F1 < 255 and F1 > 200 and F2 < 220 and F2 > 180 and F3 < 155 and F3 > 130 and F4 < 200 and F4 > 160 and F5 < 180 and F5 > 110  and not condition_flags ['C']:
				print('C')
				engine.say("C")
				engine.runAndWait()
				condition_flags['C'] = True
				condition_flags['B'] = False	

			elif F1 < 240 and F1 > 200 and F2 < 200 and F2 > 175 and F3 < 155 and F3 > 130 and F4 < 300 and F4 > 265 and F5 < 230 and F5 > 170 and not condition_flags ['D'] :
				print('D')
				engine.say("D")
				engine.runAndWait()	
				condition_flags['D'] = True
				condition_flags['C'] = False
				condition_flags['F'] = False

			elif F1 < 210 and F1 > 175 and F2 < 180 and F2 > 140 and F3 < 155 and F3 > 110 and F4 < 180 and F4 > 140 and F5 < 215 and F5 > 180  and not condition_flags ['E']:
				print('E')
				engine.say("E")
				engine.runAndWait()
				condition_flags['E'] = True
				condition_flags['D'] = False	



			elif F1 < 310 and F1 > 280 and F2 < 270 and F2 > 245 and F3 < 300 and F3 > 210 and F4 < 195 and F4 > 165 and F5 < 250 and F5 > 160  and not condition_flags ['F']:
				print('F')
				engine.say("F")
				engine.runAndWait()
				condition_flags['F'] = True
				condition_flags['E'] = False

			elif F1 < 220 and F1 > 195 and F2 < 177 and F2 > 155 and F3 < 140 and F3 > 105 and F4 < 305 and F4 > 265 and F5 < 255 and F5 > 200  and not condition_flags ['G']:
				print('G')
				engine.say("G")
				engine.runAndWait()
				condition_flags['G'] = True
				condition_flags['F'] = False
	

			
			

			
			


			print("Arduino 1 Sensor Data:", sensor_data1)
			print("Arduino 2 Sensor Data:", sensor_data2)
			

			if keyboard.is_pressed("}"):
				break
			
		except:
			print('error')


