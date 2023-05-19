import os
from colorama import init, Fore, Style

# Initialize colorama for Windows systems
init()

def remove_watermark(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        if len(lines) > 0 and lines[0].strip() == 'ï»¿// Made in NPC Maker by BowieD':
            lines = lines[1:]  # Remove the first line (watermark)
            file.seek(0)
            file.writelines(lines)
            file.truncate()
            return True
    return False

def process_directory(directory):
    modified = False
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.dat'):
                file_path = os.path.join(root, file_name)
                if remove_watermark(file_path):
                    modified = True
                    relative_path = file_path.replace(directory, '', 1).strip(os.path.sep)
                    print(f'{Fore.GREEN}Modified:{Style.RESET_ALL}', relative_path)

    if not modified:
        print(f'{Fore.YELLOW}No files modified.{Style.RESET_ALL}')

# Main program
if __name__ == '__main__':
    use_current_directory = input(f'{Fore.CYAN}Do you want to use the directory where the Python file is located? (yes/no):{Style.RESET_ALL} ')
    
    if use_current_directory.lower() == 'yes':
        directory = os.path.dirname(os.path.abspath(__file__))
    else:
        directory = input(f'{Fore.CYAN}Enter the master directory path:{Style.RESET_ALL} ')

    process_directory(directory)

    input(f'{Fore.CYAN}Press Enter to quit...{Style.RESET_ALL}')
