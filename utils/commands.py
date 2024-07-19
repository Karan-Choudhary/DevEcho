import regex as re
from utils.ml_template import create_project as ml_project
from utils.general_project_template import create_project as general_project

class Commands:
    def __init__(self):
        pass
    
    def _preprocess_text(self, text):
        text = text.lower()
        text = text.replace('dot', '.').lower()
        text = text.replace('underscore', '_')
        text = text.replace(' ', '_')
        text = text.replace(',', '')
        text = re.sub(r'\s+', ' ', text)
        return text
    
    def touch_command(self, said_text):
        partial_command = "touch"
        file_name = said_text.split('create')[1].strip()
        file_name = file_name.replace('dot', '.').lower()
        file_name = file_name.replace('underscore', '_').lower()
        file_name = re.sub(r'\s+', '', file_name)
        return f"{partial_command} {file_name}"
    
    def mkdir_command(self, said_text):
        partial_command = 'mkdir'
        dir_name = said_text.split('directory')[1].strip()
        return f"{partial_command} {dir_name}"
    
    def pkiill_command(self, said_text):
        partial_command = 'pkill -f'
        process_name = said_text.split('kill')[1].strip()
        return f"{partial_command} {process_name}"
    
    def rm_command(self, said_text):
        partial_command = 'rm -r'
        directory_name = said_text.split('delete')[1].strip()
        return f"{partial_command} {directory_name}"
    
    def show_stats(self, said_text):
        if "btop" in said_text.lower() or "b top" in said_text.lower():
            return "btop"
        elif "htop" in said_text.lower() or "h top" in said_text.lower():
            return "htop"
        return "Invalid Command"
    
    def create_ml_template(self, said_text):
        project_name = said_text.split('project')[1].strip().lower()
        project_name = self._preprocess_text(project_name)
        # partial_command = 'python3 -m utils.ml_template'
        ml_project(project_name)
        return "echo 'DONE'"
    
    def general_project_template(self, said_text):
        project_name = said_text.split('project')[1].strip().lower()
        project_name = self._preprocess_text(project_name)
        general_project(project_name)
        # partial_command = 'python3 -m utils.general_project_template'
        return "echo 'DONE'"