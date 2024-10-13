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

DYNAMIC_FUNC_MAPPINGS = {
    0: COMMAND_OBJ.mkdir_command,
    1: COMMAND_OBJ.touch_command,
    2: COMMAND_OBJ.rm_command,
    3: COMMAND_OBJ.pkiill_command,
    4: COMMAND_OBJ.show_stats,
    5: COMMAND_OBJ.create_ml_template,
    6: COMMAND_OBJ.general_project_template,
    7: COMMAND_OBJ.refactor_code,
    'create_directory': COMMAND_OBJ.mkdir_command,
    'create_file': COMMAND_OBJ.touch_command,
    'delete': COMMAND_OBJ.rm_command,
    'kill': COMMAND_OBJ.pkiill_command,
    'show_stats': COMMAND_OBJ.show_stats,
    'ml_project': COMMAND_OBJ.create_ml_template,
    'general_project': COMMAND_OBJ.general_project_template,
    'refactor': COMMAND_OBJ.refactor_code
}