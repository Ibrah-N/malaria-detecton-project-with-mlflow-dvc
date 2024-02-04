from pathlib import Path
import logging
import os

project_name = "cnnClassifier"



logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    ".gethub/workflows/.getkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/conifg/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "conifg/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)


    # make directories if already exists then let it be
    if (file_dir != ""):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for the file : {file_name}")


    # create files within the above create directories
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file : {file_name}")

    
    else:
        logging.info(f"{file_name} already exists")
    