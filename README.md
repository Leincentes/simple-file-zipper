# File Zipper GUI

This is a simple file zipper application with a graphical user interface (GUI) built using Tkinter in Python. The application allows users to select multiple files and compress them into a single zip archive.

## Features

- **Add Files**: Select multiple files to add to the zip archive.
- **Remove Selected Files**: Remove selected files from the list of files to be zipped.
- **Create Zip**: Compress the selected files into a zip archive.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your system.
3. Run the script using the command:
    ```bash
    python file_zipper.py
    ```

## Usage

1. **Add Files**: Click the "Add Files" button to select files to be zipped.
2. **Remove Selected Files**: Select files in the listbox and click "Remove Selected Files" to remove them.
3. **Create Zip**: Click the "Create Zip" button to save the selected files into a zip archive. A file dialog will prompt you to specify the location and name of the zip file.

## Code Structure

- **FileZipper Class**: Handles the GUI creation and event handling.
  - `create_widgets()`: Initializes the GUI widgets.
  - `add_files()`: Opens a file dialog to select files and adds them to the listbox and internal file list.
  - `remove_files()`: Removes selected files from the listbox and internal file list.
  - `create_zip()`: Creates a zip archive of the selected files, saving it to the user-specified location.

## Example

Run the script and a window will appear with buttons to add files, remove selected files, and create a zip archive. The listbox displays the selected files.

## License

This project is licensed under the MIT License.

