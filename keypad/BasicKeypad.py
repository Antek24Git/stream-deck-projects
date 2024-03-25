# Include Libraries
import serial
import time
import pyautogui

# Assign port variable to port used by Arduino board
com_num = input("hi, please select your com port number(numbers 1-5)\a \n")
port = "com" + com_num


# Connect to the Arduino using the serial library

arduino_data = serial.Serial(port, 9600)

# Delay for 1 second

time.sleep(1)

# Read the data sent from the arduino
while True:

    # Wait while there is no data
    while arduino_data.inWaiting() == 0:
        pass

    # Read data when avaliable
    data_packet = arduino_data.readline()

    # Convert from byte to string
    data_packet = str(data_packet, "utf-8")

    # Remove new lines
    data_packet = data_packet.strip("\r\n")

    pyautogui.hotkey("ctrl","escape")

input("this is just so if you package the code to an exe it wont close :)")