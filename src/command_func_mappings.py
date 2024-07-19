# import TYPING

from utils.commands import Commands

COMMAND_OBJ = Commands()


COMMAND_FUNC_MAPPINGS = {
    'touch': COMMAND_OBJ.touch_command,
    'mkdir': COMMAND_OBJ.mkdir_command,
    "pkill": COMMAND_OBJ.pkiill_command,
    "rm": COMMAND_OBJ.rm_command,
    'stat': COMMAND_OBJ.show_stats,
    'ml_template': COMMAND_OBJ.create_ml_template,
    'general_project_template': COMMAND_OBJ.general_project_template
}