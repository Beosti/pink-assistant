import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()
file_path_todofile = os.getenv("TEXT_FILE_PATH")

todofile = open(file_path_todofile, "r") # open the file

content = todofile.read()
parts = content.split("#")

parts_map = {} # make the map to store in, numbers and the parts of todo
new_index = 1
for index, part in enumerate(parts, start=1):
    stripped_part = part.strip()
    if stripped_part != "":
        parts_map[new_index] = stripped_part
        new_index += 1


# Done all the loading of the to-do's in a hashmap

root = tk.Tk()

for index, part in enumerate(parts, start=1):
    label = tk.Label(root, height = 3 + (index), text=str(parts_map.get(index)), font=('Arial', 12))
    label.pack(padx=20, pady=20)

root.mainloop()

