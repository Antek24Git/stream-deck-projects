import serial
import time
import pyautogui

custom_list = []
custom_list2 = []
custom_list3 = []


def ifs():
    if data_packet == "1":
        pyautogui.hotkey(custom_list.__getitem__(0))
    elif data_packet == "1" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(0) + custom_list2.__getitem__(0))
    elif data_packet == "1" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(0)
            + custom_list2.__getitem__(0)
            + custom_list3.__getitem__(0)
        )

    if data_packet == "2":
        pyautogui.hotkey(custom_list.__getitem__(1))
    elif data_packet == "2" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(1) + custom_list2.__getitem__(1))
    elif data_packet == "2" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(1)
            + custom_list2.__getitem__(1)
            + custom_list3.__getitem__(1)
        )

    if data_packet == "3":
        pyautogui.hotkey(custom_list.__getitem__(2))
    elif data_packet == "3" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(2) + custom_list2.__getitem__(2))
    elif data_packet == "3" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(2)
            + custom_list2.__getitem__(2)
            + custom_list3.__getitem__(2)
        )

    if data_packet == "A":
        pyautogui.hotkey(custom_list.__getitem__(3))
    elif data_packet == "A" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(3) + custom_list2.__getitem__(3))
    elif data_packet == "A" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(3)
            + custom_list2.__getitem__(3)
            + custom_list3.__getitem__(3)
        )

    if data_packet == "4":
        pyautogui.hotkey(custom_list.__getitem__(4))
    elif data_packet == "4" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(4) + custom_list2.__getitem__(4))
    elif data_packet == "4" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(4)
            + custom_list2.__getitem__(4)
            + custom_list3.__getitem__(4)
        )

    if data_packet == "5":
        pyautogui.hotkey(custom_list.__getitem__(5))
    elif data_packet == "5" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(5) + custom_list2.__getitem__(5))
    elif data_packet == "5" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(5)
            + custom_list2.__getitem__(5)
            + custom_list3.__getitem__(5)
        )

    if data_packet == "6":
        pyautogui.hotkey(custom_list.__getitem__(6))
    elif data_packet == "6" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(6) + custom_list2.__getitem__(6))
    elif data_packet == "6" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(6)
            + custom_list2.__getitem__(6)
            + custom_list3.__getitem__(6)
        )

    if data_packet == "B":
        pyautogui.hotkey(custom_list.__getitem__(7))
    elif data_packet == "B" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(7) + custom_list2.__getitem__(7))
    elif data_packet == "B" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(7)
            + custom_list2.__getitem__(7)
            + custom_list3.__getitem__(7)
        )

    if data_packet == "7":
        pyautogui.hotkey(custom_list.__getitem__(8))
    elif data_packet == "7" and choice_1 == "y":
        pyautogui.hotkey(custom_list.__getitem__(8) + custom_list2.__getitem__(8))
    elif data_packet == "7" and choice_2 == "y":
        pyautogui.hotkey(
            custom_list.__getitem__(8)
            + custom_list2.__getitem__(8)
            + custom_list3.__getitem__(8)
        )

        if data_packet == "8":
            pyautogui.hotkey(custom_list.__getitem__(9))
        elif data_packet == "8" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(9) + custom_list2.__getitem__(9))
        elif data_packet == "8" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(9)
                + custom_list2.__getitem__(9)
                + custom_list3.__getitem__(9)
            )

        if data_packet == "9":
            pyautogui.hotkey(custom_list.__getitem__(10))
        elif data_packet == "9" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(10) + custom_list2.__getitem__(10))
        elif data_packet == "9" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(10)
                + custom_list2.__getitem__(10)
                + custom_list3.__getitem__(10)
            )

        if data_packet == "C":
            pyautogui.hotkey(custom_list.__getitem__(11))
        elif data_packet == "C" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(11) + custom_list2.__getitem__(11))
        elif data_packet == "C" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(11)
                + custom_list2.__getitem__(11)
                + custom_list3.__getitem__(11)
            )

        if data_packet == "*":
            pyautogui.hotkey(custom_list.__getitem__(12))
        elif data_packet == "*" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(12) + custom_list2.__getitem__(12))
        elif data_packet == "*" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(12)
                + custom_list2.__getitem__(12)
                + custom_list3.__getitem__(12)
            )

        if data_packet == "0":
            pyautogui.hotkey(custom_list.__getitem__(13))
        elif data_packet == "0" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(13) + custom_list2.__getitem__(13))
        elif data_packet == "0" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(13)
                + custom_list2.__getitem__(13)
                + custom_list3.__getitem__(13)
            )

        if data_packet == "#":
            pyautogui.hotkey(custom_list.__getitem__(14))
        elif data_packet == "#" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(14) + custom_list2.__getitem__(14))
        elif data_packet == "#" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(14)
                + custom_list2.__getitem__(14)
                + custom_list3.__getitem__(14)
            )

        if data_packet == "D":
            pyautogui.hotkey(custom_list.__getitem__(15))
        elif data_packet == "D" and choice_1 == "y":
            pyautogui.hotkey(custom_list.__getitem__(15) + custom_list2.__getitem__(15))
        elif data_packet == "D" and choice_2 == "y":
            pyautogui.hotkey(
                custom_list.__getitem__(15)
                + custom_list2.__getitem__(15)
                + custom_list3.__getitem__(15)
            )

print("if this is your first time running this code please the the README.md for useful information")
# Assign port variable to port used by Arduino board
com_num = input("Please select your com port number(numbers 1-5)\n")
port = "com" + com_num

# Connect to the Arduino using the serial library
try:
    arduino_data = serial.Serial(port, 9600)
except:
    print(
        f"no arduino on com{com_num} please provide the correct com port next time.\a"
    )

# Delay for 1 second
choice_binds = input(
    """we will now configure what each of the matrix keys will press, if you have any buttons excluding utf-8 characters type:
list
if you would like to continue without a list type :
continue
if you would like a button to be in its default keybind just press enter when prompted for keybind
if you would like multiple keybinds for a single button then type your keybinds in this format:
 1, 2
 waiting for input... :"""
)
if choice_binds == "list":
    print(
        """control = ctrl
    escape = escape
    shift = shift 
    alt = alt
    f1 = f1(this applies to all f keys)
    del = delete
    type direction for arrow keys, for example 'up' for up arrow
    """
    )
elif choice_binds == "continue":
    print()

time.sleep(1)

for i in range(16):
    i += 1
    str(i)
    custom_list.append(input(f"what would you like button {i} to do? "))
    print(f"button {i} is now bound to {custom_list.__getitem__(int(i-1))}")
    int(i)
choice_1 = input(
    "do you wish to add a second keybind which would also be activated by a button? y/n \a"
)
if choice_1 == "y":
    i = 0
    for i in range(16):
        i += 1
        str(i)
        custom_list2.append(
            input(f"what would you like button {i} to do as a second keybind? ")
        )
        print(
            f"button {i} is now bound to {custom_list.__getitem__(int(i-1))} and {custom_list2.__getitem__(int(i - 1))}"
        )
        int(i)
choice_2 = input(
    "do you wish to add a third keybind which would also be activated by a button? y/n \a"
)
if choice_2 == "y":
    i = 0
    for i in range(16):
        i += 1
        str(i)
        custom_list3.append(
            input(f"what would you like button {i} to do as a third keybind? ")
        )
        print(
            f"button {i} is now bound to {custom_list.__getitem__(int(i-1))}, {custom_list2.__getitem__(int(i - 1))} and  {custom_list3.__getitem__(int(i - 1))}"
        )
        int(i)

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
    print(data_packet)
    ifs()


input("this is just so if you package the code to an exe it wont close :)")
