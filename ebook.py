import os
import subprocess

class EBook:
    def __init__(self, title, file_path):
        self.title = title
        self.file_path = file_path

    def view(self):
        subprocess.run(["epy", self.file_path])
