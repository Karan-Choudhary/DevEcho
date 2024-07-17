class Commands:
    def __init__(self):
        pass
    
    def touch_command(self, said_text):
        partial_command = "touch"
        said_text = said_text.replace('dot', '.')
        file_name = said_text.split('create')[1].strip()
        return f"{partial_command} {file_name}"
    
    def mkdir_command(self, said_text):
        partial_command = 'mkdir'
        dir_name = said_text.split('directory')[1].strip()
        return f"{partial_command} {dir_name}"