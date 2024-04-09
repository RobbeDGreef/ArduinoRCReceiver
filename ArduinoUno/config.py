# This is a configuration file
# Only change settings here if you know what you are doing and if you
# are sure it won't break the serial connection with the arduino

# Serial connection settings
CONNECTIONPORT = 'COM3'
BAUDRATE = 9600
STOPBITS = 1
PARITY = 'N'  # 'N' is off, even is 'E', odd is 'O', mark is 'M' and space is 'S'
BYTESIZE = 8

# Channel configurations
# X1 means the X axis of the leftmost stick, X2 is the X axis of the right hand stick
# The order the channels are sent in are defined in the Arduino code.
# By default it is
# 1. Throttle
# 2. Roll
# 3. Pitch
# 4. Yaw
CHANNEL_AXISES = [
    'X1',
    'Y1',
    'X2',
    'Y2',
]

# Minimum and maximum mapping of each channel
CHANNEL_MINMAX = [
    (1090, 1870),
    (1090, 1870),
    (1090, 1870),
    (1090, 1870),
]

CHANNEL_COUNT = len(CHANNEL_AXISES)

