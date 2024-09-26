import os
from utils.project_template_mappings import TEMPLATE_MAPPINGS, BOILER_CODE


def create_directories(directories, project_name=None):
    for directory in directories:
        if project_name is not None:
            directory = f"{project_name}/{directory}"
        os.makedirs(directory, exist_ok=True)

def create_files(files, project_name=None):
    for file in files:
        if project_name is not None:
            file = f"{project_name}/{file}"
            code = populate_with_code(project_name, 'python', file.split('/')[-1])
        else:
            code = populate_with_code(project_name, 'python', file)
        with open(file, 'w') as f:
            if code is not None:
                f.write(code)

def populate_with_code(project_name, language, file_name):
    try:
        file_path = BOILER_CODE[language][file_name]
        with open(file_path, 'r') as f:
            code = f.read()
        return code
    except Exception:
        return None

def start_project(project_name, project_type):
    project_info = TEMPLATE_MAPPINGS[project_type]
    project_file_info = project_info['files']
    project_dir_info = project_info['directories']
    create_directories(project_dir_info, project_name)
    create_files(project_file_info, project_name)