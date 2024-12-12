from dotenv import load_dotenv
import os

load_dotenv()
file_path_todofile = os.getenv("TEXT_FILE_PATH")

if file_path_todofile:
    print("Hello there sir! I have a few tasks for you:")
    todofile = open(file_path_todofile, "r")
    content = todofile.read()

    parts = content.split("#")

    for part in parts:
        stripped_part = part.strip()
        if stripped_part:
            print(f"- {stripped_part}")

    todofile.close()
else:
    print("TEXT_FILE_PATH is not set in the .env file")
