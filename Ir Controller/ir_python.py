import serial
from time import sleep as sl
import pyautogui

# Assign port variable to port used by Arduino board
com_num = input("hi, please select your com port number(numbers 1-5)\a \n")
port = "com" + com_num

# Connect to the Arduino using the serial library
# noinspection PyBroadException
try:
    arduino_data = serial.Serial(port, 9600)
except:
    print(
        f"no arduino on com{com_num} please provide the correct com port next time.\a"
    )
# Delay for 1 second

sl(1)

# Read the data sent from the arduino
while True:

    # Wait while there is no data
    # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
    while arduino_data.inWaiting() == 0:
        pass

    # Read data when available
    data_packet = arduino_data.readline()

    # Convert from byte to string
    data_packet = str(data_packet, "utf-8")

    # Remove new lines
    data_packet = data_packet.strip("\r\n")
    print(data_packet)
    if int(data_packet) <= 9:
        pyautogui.hotkey(str(data_packet))

    if int(data_packet) >= 13:
        data_packet = int(data_packet) - 12
        pyautogui.hotkey("win", str(data_packet))

    if data_packet == "10":
        pyautogui.hotkey("ctrl", "shift", "escape")

    if data_packet == "11":
        pyautogui.hotkey("win", "alt", "prtsc")

    if data_packet == "12":
        pyautogui.hotkey("win", "r")


input("this is just so if you package the code to an exe it wont close :)")
