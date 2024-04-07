import os
from ebookmanager import EBookManager

class EBookApp:
    def __init__(self):
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.config_file = os.path.join(self.script_path, "config.txt")
        self.ebook_path = os.path.join(self.script_path, "ebooks")
        self.download_path = os.path.join(self.script_path, "books")
        os.makedirs(self.ebook_path, exist_ok=True)
        os.makedirs(self.download_path, exist_ok=True)
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as file:
                config_path = file.read().strip()
                if os.path.exists(config_path):
                    self.ebook_path = config_path
                else:
                    print(f"Configured path '{config_path}' does not exist. Using default path.")
        self.save_config()

    def save_config(self):
        with open(self.config_file, "w") as file:
            file.write(self.ebook_path)

    def set_config_path(self):
        path = input("Enter the new path for the configuration file: ")
        self.config_file = path
        self.load_config()
        print("Configuration file path updated successfully.")

    def set_ebook_path(self):
        path = input("Enter the new path for ebooks: ")
        if os.path.exists(path):
            self.ebook_path = path
            self.save_config()
            print("EBook path updated successfully.")
        else:
            print("Invalid path. Path does not exist.")

    def run(self):
        self.manager = EBookManager(self.ebook_path, self.download_path)
        while True:
            try:
                print("\nTerminal EBook Manager")
                print("1. List EBooks")
                print("2. View EBook")
                print("3. Download EBook")
                print("4. Set EBook Path")
                print("5. Set Configuration Path")
                print("6. Quit")
                choice = input("Enter your choice (1-6): ")

                if choice == "1":
                    ebooks = self.manager.list_ebooks()
                    print("EBooks:")
                    for ebook in ebooks:
                        print(ebook.title)
                elif choice == "2":
                    self.manager.view_ebook()
                elif choice == "3":
                    self.manager.download_ebook()
                elif choice == "4":
                    self.set_ebook_path()
                elif choice == "5":
                    self.set_config_path()
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

            except KeyboardInterrupt:
                print("\033[91m\nAre you sure you want to exit? Press Ctrl+C again to exit or Enter to go back.\033[0m")
                try:
                    input()
                except KeyboardInterrupt:
                    print("\nExiting the application...")
                    break
