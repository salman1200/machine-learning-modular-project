import os
from pathlib import Path
import logging

while True:
    project_name = input('Enter your project name: ')
    if project_name != '':
        break

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/models/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"config/config.yaml",
    f"schema.yaml",
    f"app.py",
    f"main.py",
    f"logs.py",
    f"exceptions.py",
    f"setup.py",
]

for file in list_of_files:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    if ((not os.path.exists(file_path)) or (os.path.getsize(file_path)) == 0):
        with open(file_path, 'w') as f:
            pass
    else:
        logging.info(f"file is already present at: {file_path}")

