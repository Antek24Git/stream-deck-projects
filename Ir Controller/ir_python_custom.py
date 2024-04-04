import serial
from time import sleep as sl
import pyautogui

custom_list = []
custom_list2 = []
custom_list3 = []

print(
    "if this is your first time running this code please read the README.md for useful information"
)
# Assign port variable to port used by Arduino board
com_num = input("Please select your com port number(numbers 1-5)\n")
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
choice_binds = input(
    """we will now configure what each of the top 9 buttons of the ir controller will hotkey, if you have any buttons excluding utf-8 
    characters type:list if you would like to continue without a list type :continue
     waiting for input... :"""
)
if choice_binds == "list":
    print(
        """\n note: when setting up the controller dont just hotkey the control button, you actually have to type the name of the button as indicated in the list.
        control = ctrl
    escape = escape
    shift = shift 
    alt = alt
    f1 = f1(this applies to all f keys)
    delete = del 
    tab = tab
    type direction for arrow keys, for example 'up' for up arrow
        """
    )
elif choice_binds == "continue":
    print()

for i in range(9):
    i += 1
    str(i)
    custom_list.append(input(f"what would you like button {i} to do? "))
    print(f"\nbutton {i} is now bound to {custom_list.__getitem__(int(i - 1))}")
    int(i)

choice_2 = input("would you like to add a second keybind? y/n :".lower())

if choice_2 == "y":
    for i in range(9):
        i += 1
        str(i)
        custom_list2.append(
            input(f"what would you like button {i} to have as a second keybind? ")
        )
        print(f"button {i} is now bound to {custom_list2.__getitem__(int(i - 1))}")
        int(i)
choice_3 = input("would you like to add a third keybind? y/n :".lower())

if choice_3 == "y" and choice_2 == "y":
    for i in range(9):
        i += 1
        str(i)
        custom_list3.append(
            input(f"what would you like button {i} to have as a third keybind? ")
        )
        print(f"button {i} is now bound to {custom_list3.__getitem__(int(i - 1))}")

print("\a The controller is now configured.")


def ifs_1_value():
    if data_packet == "1":
        pyautogui.hotkey(custom_list.__getitem__(0))

    if data_packet == "2":
        pyautogui.hotkey(custom_list.__getitem__(1))

    if data_packet == "3":
        pyautogui.hotkey(custom_list.__getitem__(2))

    if data_packet == "4":
        pyautogui.hotkey(custom_list.__getitem__(3))

    if data_packet == "5":
        pyautogui.hotkey(custom_list.__getitem__(4))

    if data_packet == "6":
        pyautogui.hotkey(custom_list.__getitem__(5))

    if data_packet == "7":
        pyautogui.hotkey(custom_list.__getitem__(6))

    if data_packet == "8":
        pyautogui.hotkey(custom_list.__getitem__(7))

    if data_packet == "9":
        pyautogui.hotkey(custom_list.__getitem__(8))


def ifs_2_value():
    if data_packet == "1":
        pyautogui.hotkey(custom_list.__getitem__(0), custom_list2.__getitem__(0))

    if data_packet == "2":
        pyautogui.hotkey(custom_list.__getitem__(1), custom_list2.__getitem__(1))

    if data_packet == "3":
        pyautogui.hotkey(custom_list.__getitem__(2), custom_list2.__getitem__(2))

    if data_packet == "4":
        pyautogui.hotkey(custom_list.__getitem__(3), custom_list2.__getitem__(3))

    if data_packet == "5":
        pyautogui.hotkey(custom_list.__getitem__(4), custom_list2.__getitem__(4))

    if data_packet == "6":
        pyautogui.hotkey(custom_list.__getitem__(5), custom_list2.__getitem__(5))

    if data_packet == "7":
        pyautogui.hotkey(custom_list.__getitem__(6), custom_list2.__getitem__(6))

    if data_packet == "8":
        pyautogui.hotkey(custom_list.__getitem__(7), custom_list2.__getitem__(7))

    if data_packet == "9":
        pyautogui.hotkey(custom_list.__getitem__(8), custom_list2.__getitem__(8))


def ifs_3_value():
    if data_packet == "1":
        pyautogui.hotkey(
            custom_list.__getitem__(0),
            custom_list2.__getitem__(0),
            custom_list3.__getitem__(0),
        )

    if data_packet == "2":
        pyautogui.hotkey(
            custom_list.__getitem__(1),
            custom_list2.__getitem__(1),
            custom_list3.__getitem__(1),
        )

    if data_packet == "3":
        pyautogui.hotkey(
            custom_list.__getitem__(2),
            custom_list2.__getitem__(2),
            custom_list3.__getitem__(2),
        )

    if data_packet == "4":
        pyautogui.hotkey(
            custom_list.__getitem__(3),
            custom_list2.__getitem__(3),
            custom_list3.__getitem__(3),
        )

    if data_packet == "5":
        pyautogui.hotkey(
            custom_list.__getitem__(4),
            custom_list2.__getitem__(4),
            custom_list3.__getitem__(4),
        )

    if data_packet == "6":
        pyautogui.hotkey(
            custom_list.__getitem__(5),
            custom_list2.__getitem__(5),
            custom_list3.__getitem__(5),
        )

    if data_packet == "7":
        pyautogui.hotkey(
            custom_list.__getitem__(6),
            custom_list2.__getitem__(6),
            custom_list3.__getitem__(6),
        )

    if data_packet == "8":
        pyautogui.hotkey(
            custom_list.__getitem__(7),
            custom_list2.__getitem__(7),
            custom_list3.__getitem__(7),
        )

    if data_packet == "9":
        pyautogui.hotkey(
            custom_list.__getitem__(8),
            custom_list2.__getitem__(8),
            custom_list3.__getitem__(8),
        )


while True:

    # Wait while there is no data
    # noinspection PyUnboundLocalVariable,PyUnresolvedReferences
    while arduino_data.inWaiting() == 0:
        pass

    # Read data when available
    data_packet = arduino_data.readline()

    # Convert from byte to string
    data_packet = str(data_packet, "utf-8")

    # Remove new lines
    data_packet = data_packet.strip("\r\n")
    print(data_packet)
    if choice_2 == "y":
        ifs_2_value()
    elif choice_2 == "y" and choice_3 != "y":
        ifs_3_value()
    else:
        ifs_1_value()
    sl(0.1)
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
