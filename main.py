import tkinter as tk
from tkinter import filedialog
import time
import sys
import os

if __name__ == "__main__":
    # Prompt for input folder
    input('Hit enter to select input folder.')
    input_path = filedialog.askdirectory(title='Select Input Folder')

    # Prompt for output folder
    input('Hit enter to select output folder.')
    output_path = filedialog.askdirectory(title='Select Output Folder')

    print('Watching {}'.format(input_path))

    time_waited = 0
    # Try/catch Keyboard interrupt
    try:
        while True:
            # Check for changes in input folder
            changes = False

            # If changes have occured, then process
            if changes:
                # Convert

                # Move file
                pass
            # Else wait then continue checking
            else:
                time.sleep(1)  # wait two seconds
                sys.stdout.write('\r{}s elapsed.'.format(time_waited))
                time_waited += 1
    except KeyboardInterrupt:
        print('\nProgram was terminated by user.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    # Begin Loop
    pass
    
