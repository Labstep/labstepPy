#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import labstep
import time
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

USER_NAME = os.getenv('LABSTEP_USERNAME')
API_KEY = os.getenv('LABSTEP_API_KEY')

# Authenticate Labstep User
user = labstep.authenticate(USER_NAME, API_KEY)

# Select device

device = user.getDevice(2314)

print(f'Connected to {device.name}')


# Define what to do when data is detected
def onDataDetected(event):
    device.addData(
      fieldName='Raw Data File',
      fieldType='file',
      filepath=event.src_path
    )


# Use watchdog built in regex event handler
# This will detect files that end in .csv
my_event_handler = RegexMatchingEventHandler([r".*\.csv$"])
# Set the handler for when files are created
my_event_handler.on_created = onDataDetected
# Set up the watchdog observer to watch a specific folder
my_observer = Observer()
path = '/path/to/device/output/folder'
my_observer.schedule(my_event_handler, path)
# Start the observer
my_observer.start()

# Set up loop to stop the script terminating unless interupted
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
