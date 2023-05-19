# THIS PROGRAM IS FOR PRIVATE USE TO REMOVE A SPECIFIC WATERMARK, NO HATE TO THE ORIGINAL DEVELOPER WHO PLACED A SCRIPT THAT PUTS WATERMARKS INTO ALL HIS FILES :)

# WaterMarkRemover

The Watermark Removal Tool is a Python script that removes a specific watermark from files in a given directory. It searches for files with the extension `.dat` and removes the watermark if it exists.

## Features

- Removes a specific watermark from files in a directory.
- Supports both relative and absolute directory paths.
- Provides colored console output to indicate modified files.

## Prerequisites

- Python 3.x
- `colorama` package (install via `pip install colorama`)

## Usage

1. Clone or download the repository to your local machine.

2. Install the required `colorama` package by running the following command:

   ```shell
   pip install colorama
3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script using the following command:

   ```shell
   python watermark_removal.py
5. The script will prompt you to choose the directory where the watermark removal should be performed. You can either use the current directory or enter a master directory path.

6. Once you provide the directory path, the script will process the files in the specified directory and its subdirectories, removing the watermark if found.

7. If any files are modified, the script will display the relative paths of the modified files in green color.

8. If no files are modified, the script will display a "No files modified" message in yellow color.

9. Press Enter to quit the script.

## Contributing
- Contributions are welcome! If you find any issues or want to enhance the functionality of the script, please feel free to open an issue.


Feel free to copy and use this README file for your project!
