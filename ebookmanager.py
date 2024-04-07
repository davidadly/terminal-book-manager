import os
import json
import subprocess
from ebook import EBook

class EBookManager:
    def __init__(self, ebook_folder):
        self.ebook_folder = ebook_folder
        self.last_selected_file = os.path.join(self.ebook_folder, "last_selected.json")
        self.create_last_selected_file()

    def create_last_selected_file(self):
        if not os.path.exists(self.last_selected_file):
            with open(self.last_selected_file, "w") as file:
                json.dump({}, file)

    def list_ebooks(self):
        ebooks = []
        for file_name in os.listdir(self.ebook_folder):
            if file_name.endswith(".epub") or file_name.endswith(".pdf"):
                file_path = os.path.join(self.ebook_folder, file_name)
                ebook = EBook(file_name, file_path)
                ebooks.append(ebook)
        return ebooks

    def view_ebook(self):
        print("\nSelect an option:")
        print("1. List all ebooks")
        print("2. Search for an ebook by name")
        choice = input("Enter your choice (1-2): ")

        ebooks = self.list_ebooks()

        # Load last selected ebook if exists
        try:
            with open(self.last_selected_file, "r") as file:
                last_selected = json.load(file)
                last_selected_title = last_selected.get("last_selected_title", "")
                if last_selected_title:
                    ebooks.sort(key=lambda x: x.title != last_selected_title)
        except Exception as e:
            print(f"Error loading last selected ebook: {str(e)}")

        if choice == "1":
            if not ebooks:
                print("No ebooks found.")
                return
            print("\nEBooks:")
            for i, ebook in enumerate(ebooks, start=1):
                print(f"{i}. {ebook.title}")
        elif choice == "2":
            query = input("Enter the beginning of the ebook name to search: ").lower()
            filtered_ebooks = [eb for eb in ebooks if eb.title.lower().startswith(query)]
            
            if not filtered_ebooks:
                print("No ebooks found matching your query.")
                return
                
            print("\nFiltered EBooks:")
            for i, ebook in enumerate(filtered_ebooks, start=1):
                print(f"{i}. {ebook.title}")
        else:
            print("Invalid choice.")
            return

        selection = input("Enter the number of the ebook you want to view: ")
        try:
            index = int(selection) - 1
            selected_ebooks = ebooks if choice == "1" else filtered_ebooks
            if 0 <= index < len(selected_ebooks):
                ebook = selected_ebooks[index]

                # Save last selected ebook
                with open(self.last_selected_file, "w") as file:
                    json.dump({"last_selected_title": ebook.title}, file)

                ebook.view()
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def download_ebook(self):
        try:
            subprocess.run(["libgen-downloader"], check=True)
        except FileNotFoundError:
            print("libgen-downloader is not installed.")
            print("Please install it using the following command:")
            print("npm i -g libgen-downloader")
        except subprocess.CalledProcessError as e:
            print("An error occurred while running libgen-downloader:")
            print(str(e))
