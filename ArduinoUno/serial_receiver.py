import serial
import vgamepad as vg
from config import *

_running = True


def remap(value, min1, max1, min2, max2):
    return int(min2 + (value - min1) * (max2 - min2) / (max1 - min1))

def translate_value(value, minmax):
    return remap(value, minmax[0], minmax[1], -1.0, 1.0)

def open_serial():
    try:
        ser = serial.Serial(port=CONNECTIONPORT, baudrate=BAUDRATE, bytesize=BYTESIZE, parity=PARITY, stopbits=STOPBITS)
    except serial.SerialException as e:
        print("Failed to open a serial connection to the arduino.")
        print("Is the correct COM port selected in the config.py file?")
        print("Error message:\n", e)
        exit(1)

    return ser


def main():
    # First setup the serial connection
    ser = open_serial()
    print("Serial connected to ", CONNECTIONPORT)

    # Then create the gamepad
    try:
        gamepad = vg.VX360Gamepad()
    except Exception as e:
        print("Failed to create virtual gamepad device.")
        print("Are the vgamepad drivers installed?")
        print("Error message:\n", e)
        exit(1)

    print("Virtual gamepad connection made")

    gamepad.reset()

    print("Mainloop started without any problems")
    print("\n")
    print("Now translating serial data to joystick controls\nDo not close the window unless you want to stop the dirver or unplugged your arduino")

    while _running:
        startbyte = ser.read(1)
        if startbyte != b'\x00':
            continue

        values = []
        for i in range(CHANNEL_COUNT):
            values.append(int.from_bytes(ser.read(2), "big"))

        # Remap the values from raw to joystick values
        for i, v in enumerate(values):
            values[i] = translate_value(v, CHANNEL_MINMAX[i])

        channel_to_value_map = {c: i for i, c in enumerate(CHANNEL_AXISES)}

        x1 = values[channel_to_value_map['X1']]
        y1 = values[channel_to_value_map['Y1']]
        x2 = values[channel_to_value_map['X2']]
        y2 = values[channel_to_value_map['Y2']]


        gamepad.left_joystick(x_value_float=x1, y_value_float=y1)
        gamepad.right_joystick(x_value_float=x2, y_value_float=y2)

        gamepad.update()


if __name__ == '__main__':
    main()
