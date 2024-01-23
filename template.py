# Import 'os' for operating system functionalities
import os

# Import 'Path' from 'pathlib' for file system path operations
from pathlib import Path

# Import 'logging' for logging events and messages
import logging

# Set basic configuration for logging: level INFO and custom message format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


# Define the name of the project
project_name = "mlProject"


# List containing paths of directories and files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]

# Iterate through the list of files to create them along with their directories
for filepath in list_of_files:
    
    # Convert string path to Path object for better handling
    filepath = Path(filepath)
    
    # Split the filepath into directory and file name
    filedir, filename = os.path.split(filepath)

    # If the directory does not exist, create it
    if filedir !="":
        
        # Create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create an empty file if it does not exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        
        # Open the file in write mode
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")