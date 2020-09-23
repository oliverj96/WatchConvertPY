import tkinter as tk
from tkinter import filedialog
import time
import sys
import os
import moviepy.editor as moviepy

if __name__ == "__main__":
    # Prompt for input and output folder
    input('Hit enter to select input and output folder.')
    input_path = filedialog.askdirectory(title='Select Input Folder')
    output_path = filedialog.askdirectory(title='Select Output Folder')

    # If directories are the same, ask user for different directories
    while input_path == output_path:
        input('Directories cannot be the same. Hit enter to select input and output folder.')    
        input_path = filedialog.askdirectory(title='Select Input Folder')
        output_path = filedialog.askdirectory(title='Select Output Folder')

    print('Watching {}'.format(input_path))

    time_waited = 0  # time since last process (seconds)
    # Try/catch Keyboard interrupt
    try:
        while True:
            # Check for changes in input folder
            files = os.listdir(input_path)

            # If changes have occured, then process
            if len(files) > 0:
                print('\nFiles detected: {}'.format(files))
                # Convert each file
                for curr_file in files:
                    print('Converting {}'.format(curr_file))
                    full_path = os.path.join(input_path, curr_file)
                    full_out = os.path.join(output_path, 'test.mp4')
                    clip = moviepy.VideoFileClip(full_path)
                    clip.write_videofile(full_out)
                    print('Done.\n')
                    os.remove(full_path)
                # Move file
                time_waited = 0
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
