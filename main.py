import os
import shutil
from datetime import datetime
from colorama import init, Fore, Style

    # Initialize colorama
init(autoreset=True)

def organize_by_type(folder_path, action="move"):
        moved = 0

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                ext = filename.split('.')[-1].lower()

                if action == "move":
                    target_folder = os.path.join(folder_path, ext.upper() + 's')
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                elif action == "rename":
                    new_filename = f"{ext.upper()}_{filename}"
                    new_path = os.path.join(folder_path, new_filename)
                    os.rename(file_path, new_path)

                moved += 1

        if action == "move":
            print(Fore.GREEN + f"{moved} file(s) organized into folders by type.")
        elif action == "rename":
            print(Fore.GREEN + f"{moved} file(s) renamed with type prefix.")


def organize_by_date(folder_path, action="move"):
        moved = 0

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                mod_time = os.path.getmtime(file_path)
                folder_name = datetime.fromtimestamp(mod_time).strftime('%Y-%m')

                if action == "move":
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                elif action == "rename":
                    new_filename = f"{folder_name}_{filename}"
                    new_path = os.path.join(folder_path, new_filename)
                    os.rename(file_path, new_path)

                moved += 1

        if action == "move":
            print(Fore.GREEN + f"{moved} file(s) organized into folders by date.")
        elif action == "rename":
            print(Fore.GREEN + f"{moved} file(s) renamed with date prefix.")


def main():
        print(Fore.CYAN + Style.BRIGHT + "📂 Welcome to File Organizer!")

        base_path = os.path.dirname(os.path.abspath(__file__))
        folder_name = input(Fore.YELLOW + "📁 Enter the folder name to organize: ").strip()
        folder = os.path.join(base_path, folder_name)

        if not os.path.exists(folder):
            print(Fore.RED + "❌ Folder does not exist.")
            return

        print(Fore.MAGENTA + f"🔎 Looking in folder: {folder}")

        method = input(Fore.YELLOW + "🔧 Choose organization method ('type' or 'date'): ").strip().lower()
        action = input(Fore.YELLOW + "🛠️  Do you want to 'move' files into folders or just 'rename' them? ").strip().lower()

        if method not in ['type', 'date'] or action not in ['move', 'rename']:
            print(Fore.RED + "❗ Invalid input. Please choose 'type' or 'date' and 'move' or 'rename'.")
            return

        if method == 'type':
            organize_by_type(folder, action)
        else:
            organize_by_date(folder, action)


if __name__ == "__main__":
        main()
