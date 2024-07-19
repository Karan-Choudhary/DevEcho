import os

DIRECTORIES = [
    'src', 'utils'
]

FILES = [
    'src/main.py', 'utils/sample.py'
]

def create_directories(project_name=None):
    for directory in DIRECTORIES:
        if project_name is not None:
            directory = f"{project_name}/{directory}"
        os.makedirs(directory, exist_ok=True)

def create_files(project_name=None):
    for file in FILES:
        if project_name is not None:
            file = f"{project_name}/{file}"
        with open(file, 'w') as f:
            pass

def create_project(project_name):
    os.makedirs(f"{project_name}", exist_ok=True)
    create_directories(project_name)
    create_files(project_name)

def main():
    create_directories()
    create_files()


if __name__ == '__main__':
    main()