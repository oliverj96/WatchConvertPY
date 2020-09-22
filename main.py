import time
import sys
import os

if __name__ == "__main__":
    # Prompt for input folder
    input('Hit enter to select input folder.')

    # Prompt for output folder
    input('Hit enter to select output folder.')

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
                time.sleep(2)  # wait two seconds
    except KeyboardInterrupt:
        print('\nProgram was terminated by user.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    # Begin Loop
    pass
    
