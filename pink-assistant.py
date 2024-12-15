from dotenv import load_dotenv
import os

load_dotenv()
file_path_todofile = os.getenv("TEXT_FILE_PATH")

if file_path_todofile:
    print("Hello there sir! I have a few tasks for you:")
    todofile = open(file_path_todofile, "r")
    content = todofile.read()

    parts = content.split("#")
    
    parts_map = {}

    for index, part in enumerate(parts, start=1):
        stripped_part = part.strip()
        parts_map[index] = stripped_part
        if stripped_part:
            print(f"- {stripped_part}")
   
    print("Do you want to delete a todo?: y/n")
    delete = input()
    if delete == "y":
        print("To delete a todo, just press the number of the part:")
        part_number = input()
        part_number = int (part_number)
        if part_number in parts_map:
            print(f"Deleted the to-do {part_number}")
            with open(file_path_todofile, "r") as todofile:
                lines = todofile.readlines()
            del lines[part_number - 1]
            with open(file_path_todofile, "w") as file:
                file.writelines(lines)
        else:
            print(parts_map)
            print(f"No number {part_number} in the to-do")
    else:
        print("good luck sir!")
    todofile.close()
else:
    print("TEXT_FILE_PATH is not set in the .env file")
