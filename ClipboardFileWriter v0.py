import os
import pyperclip
import time

def save_clipboard_to_file(mode='off'):
    # Get the text from the clipboard
    text = pyperclip.paste()
    
    if mode == 'off':
        # Default folder path and file extension
        folder = os.path.join(os.path.expanduser('~'), 'Desktop')
        extension = '.txt'
    elif mode == 'on':
        # Prompt the user to enter the folder path and file extension
        folder = input('Enter the folder path (e.g. C:/Users/User/Documents/): ')
        extension = input('Enter the file extension (e.g. .txt, .py): ')
    else:
        # Invalid mode
        print('Error: Invalid mode. Mode must be either "on" or "off".')
        return None
    
    # Generate the filename using the timestamp
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = os.path.join(folder, timestamp + extension)
    
    # Check if the folder exists
    if not os.path.exists(folder):
        print(f'Error: Folder "{folder}" does not exist.')
        return None
    
    # Check if the file already exists
    if os.path.exists(filename):
        # Prompt the user for confirmation before overwriting
        overwrite = input(f'File "{filename}" already exists. Overwrite? (yes/no): ')
        if overwrite.lower() != 'yes':
            print('Aborted.')
            return None
    
    # Write the text to the file
    with open(filename, 'w') as f:
        f.write(text)
    
    # Print a message indicating the path of the saved file
    print(f'Saved to {filename}')
