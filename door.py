import os
b = 'A0B0C0D0E0'
found = 0
with open("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0") as reader:
	
	with open("users.txt") as users:
		for line in users:
			if b in line:
				print("FOUND")
				found = 1
		users.close()
		if found == 0:
			print("NOT FOUND.")
		reader.close()
 
