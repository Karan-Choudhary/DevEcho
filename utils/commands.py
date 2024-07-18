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
    
    def pkiill_command(self, said_text):
        partial_command = 'pkill -f'
        process_name = said_text.split('kill')[1].strip()
        return f"{partial_command} {process_name}"
    
    def rm_command(self, said_text):
        partial_command = 'rm -r'
        directory_name = said_text.split('delete')[1].strip()
        return f"{partial_command} {directory_name}"