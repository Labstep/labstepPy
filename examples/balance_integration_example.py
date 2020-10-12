#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep
import serial

# Authenticate Labstep User
user = labstep.authenticate('myaccount@labstep.com', 'APIKEY')

# Select device

device = user.getDevice(2314)

print(f'Connected to {device.name}')

# Open Serial Port to Device
ser = serial.Serial(port='/dev/ttyACM0', timeout=2)

# Flush input to avoid data overlap and start fresh
ser.flushInput()

# Set up loop to continuously monitor data from device
try:
    while True:
        # Read line of data stream
        raw_input = ser.readline()

        # Strip new line characters from the end of the data.
        stripped_input = raw_input[0:len(raw_input)-2]

        # Decode the raw bytes data to a float
        decoded_input = float(stripped_input.decode("utf-8"))

        print(decoded_input)

        # Send data to Labstep

        device.addData(
          fieldName='Temperature',
          fieldType='numeric',
          number=decoded_input,
          unit='K')
except KeyboardInterrupt:
    print('Stopping')
