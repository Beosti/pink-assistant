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
   
    print("Do you want to (a)dd/(d)elete/(n)othing to the todo?: ")
    input_action = input()
    if input_action == "d":
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
    elif input_action == "a":
        print("What to-do would you like to add: ")
        input_addition = input()
        with open(file_path_todofile, "r") as file:
            lines = file.readlines()
        lines.append("\n# " + input_addition)
        with open(file_path_todofile, "w") as todofile:
            todofile.writelines(lines)
    elif input_action == "n":
        print("good luck sir!")
    else:
        print("not a good input!")
    todofile.close()
else:
    print("TEXT_FILE_PATH is not set in the .env file")
